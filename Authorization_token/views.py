import logging
import os

from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from .models import TokenForRegistration, AuthorizationUserOnToken
from .openapi_responses import check_registration_key, user_logout
from .serializers import UserDataSerializer, UserLoginSerializer, \
    UserWithAccessTokenSerializer, UpdateUserInfoSerializer, UserAccessSuccessSerializer, TelegramTokenSerializer, \
    AccessTokenSerializer

logger = logging.getLogger(__name__)


class LogoutUser(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['User'],
        responses={
            200: user_logout
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({
                'success': 'Пользователь успешно вышел из системы'},
                status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'error': 'Не удалось завершить сеанс'},
                status=status.HTTP_400_BAD_REQUEST)


class CheckAuthorizationUser(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['User'],
        responses={
            200: UserAccessSuccessSerializer
        }
    )
    def post(self, request):
        try:
            user = request.user
            if not user:
                raise InvalidToken('Пользователь не найден')

            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token

            serializer = UserAccessSuccessSerializer({
                'success': True,
                'access_token': str(access_token),
                'user_data': user
            })

            return Response(serializer.data, status=status.HTTP_200_OK)
        except TokenError:
            return Response(
                {'error': 'Пользователь не найден'},
                status=status.HTTP_400_BAD_REQUEST)


class RefreshUserProfile(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        tags=['User'],
        request=UserDataSerializer,
        responses={
            200: UserAccessSuccessSerializer
        }
    )
    def post(self, request):
        user = request.user
        serializer = UserDataSerializer(user, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(
                {'errors': 'Введены некорректные данные для обновления профиля'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save()

        refresh_token = RefreshToken.for_user(user)
        access_token = refresh_token.access_token

        serializer = UserAccessSuccessSerializer({
            'success': True,
            'access_token': str(access_token),
            'user_data': user,
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class CheckRegistrationKey(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['User'],
        request=TelegramTokenSerializer,
        responses={
            200: check_registration_key
        }
    )
    def post(self, request):
        registration_token = request.data.get('registration_token')
        if registration_token is None:
            return Response(
                {'errors': 'Токен не был передан'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            token_info = get_object_or_404(TokenForRegistration, registration_token=registration_token)
            return Response({
                'checkStatus': True
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'checkStatus': False
            }, status=status.HTTP_200_OK)


class RegistrationWithToken(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['User'],
        request=UserWithAccessTokenSerializer,
        parameters=[
            OpenApiParameter('key', str, description='Registration token for user registration', required=True)
        ],
        responses={
            200: UpdateUserInfoSerializer
        }
    )
    def post(self, request):
        registration_token = request.query_params.get('key')
        token_info = get_object_or_404(TokenForRegistration, registration_token=registration_token)
        user = token_info.user

        serializer = UpdateUserInfoSerializer(user, data=request.data, partial=True)

        if not serializer.is_valid():
            return Response(
                {'errors': 'Некорректные данные для регистрации'},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        serializer = UpdateUserInfoSerializer({
            'registration_token': registration_token,
            'access_token': str(access),
            'user_data': UserDataSerializer(user).data
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginWithToken(APIView):
    permission_classes = [AllowAny]

    # authentication_classes = [AllowAnyAuthentication]

    @extend_schema(
        tags=['User'],
        request=UserLoginSerializer,
        responses={
            200: UserWithAccessTokenSerializer
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                {'errors': 'Некорректные данные для входа'},
                status=status.HTTP_400_BAD_REQUEST
            )

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        if username is None or password is None:
            return Response({'error': 'Нужно ввести логин и пароль'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({'error': 'Неверные данные для входа'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        refresh_token_expiration = refresh['exp']  # Время окончания в формате Unix
        refresh_token_expiration_datetime = timezone.datetime.fromtimestamp(refresh_token_expiration)

        formatted_refresh_token_expiration = refresh_token_expiration_datetime.strftime("%d.%m.%Y - %H:%M")
        create_token = user.created.strftime("%d.%m.%Y - %H:%M")

        log_line = (f"\nuser_id: {user.id}\n"
                    f"username: {user.username}\n"
                    f"access_token: {str(access)}\n"
                    f"refresh_token: {str(refresh)}\n"
                    f"created_token: {create_token}\n"
                    f"refresh_token_expires_at: {formatted_refresh_token_expiration}\n")

        directory = '/home/aleks/CoD/Django/VideoSpace_API/users_info/'

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, f'{user.username}.txt')

        with open(file_path, 'a') as file:
            file.write(log_line)

        logger.info("Пользователь %s вошел успешно", user.username)

        serializer = UserWithAccessTokenSerializer({
            'access_token': str(access),
            'user_data': UserDataSerializer(user).data
        })

        return Response(serializer.data, status=status.HTTP_200_OK)


class RefreshAccessToken(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        tags=['User'],
        request=AccessTokenSerializer,
        responses={
            200: AccessTokenSerializer
        },
    )

    def post(self, request):
        old_access_token = request.data.get('access_token')

        if not old_access_token:
            return Response({'error': 'Access token not provided'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            decoded_token = AccessToken(old_access_token)
            user_id = decoded_token['user_id']
            user = AuthorizationUserOnToken.objects.filter(id=user_id).first()
            if not user:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

            refresh = RefreshToken.for_user(user)
            new_access_token = refresh.access_token

            return Response({
                'new_access_token': str(new_access_token)
            })
        except TokenError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
