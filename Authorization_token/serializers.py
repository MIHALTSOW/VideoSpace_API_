from enum import unique

from rest_framework import serializers

from Authorization_token.models import AuthorizationUserOnToken, TokenForRegistration


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=50)


class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizationUserOnToken
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'created', 'changed', 'password']


class UserWithAccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(read_only=True)
    user_data = UserDataSerializer()


class UpdateUserInfoSerializer(serializers.Serializer):
    registration_token = serializers.CharField(required=True, max_length=50)
    access_token = serializers.CharField(read_only=True)
    user_data = UserDataSerializer()

    def update(self, instance, validated_data):
        # Обновляем поля пользователя
        user_data = validated_data.get('user_data', {})
        instance.first_name = user_data.get('first_name', instance.first_name)
        instance.last_name = user_data.get('last_name', instance.last_name)
        instance.email = user_data.get('email', instance.email)
        instance.username = user_data.get('username', instance.username)

        # Обновляем пароль, если он есть
        password = user_data.get('password')
        if password and password.strip():
            instance.set_password(password)  # Убедитесь, что используете set_password для хеширования пароля
        else:
            raise serializers.ValidationError({'password': 'Пароль не может быть пустым'})

        instance.save()  # Сохраняем изменения в модели
        return instance


class UserAccessSuccessSerializer(serializers.Serializer):
    success = serializers.CharField(max_length=50)
    access_token = serializers.CharField(read_only=True)
    user_data = UserDataSerializer()


class TelegramTokenSerializer(serializers.Serializer):
    registration_token = serializers.CharField(required=True, max_length=50)


class AccessTokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True, max_length=50)
