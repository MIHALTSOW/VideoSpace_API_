"""
URL configuration for VideoSpace_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from Authorization_token.views import (
    CheckAuthorizationUser,
    CheckRegistrationKey,
    LoginWithToken,
    LogoutUser,
    RefreshAccessToken,
    RefreshUserProfile,
    RegistrationWithToken,
)
from Likes.views import CreateLikeView, GetUserLikes
from media_stream.views import PhotoList, VideoList

router = DefaultRouter()
router.register(r"api/photos", PhotoList, basename="photo")
router.register(r"api/videos", VideoList, basename="video")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api/login", LoginWithToken.as_view(), name="login"),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh_access/",
        RefreshAccessToken.as_view(),
        name="token_refresh_access",
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/registration",
        RegistrationWithToken.as_view(),
        name="registration",
    ),
    path(
        "api/check-registration-key",
        CheckRegistrationKey.as_view(),
        name="check_registration_key",
    ),
    path(
        "api/auth",
        CheckAuthorizationUser.as_view(),
        name="check_authorization_user",
    ),
    path(
        "api/refresh_profile",
        RefreshUserProfile.as_view(),
        name="refresh_profile",
    ),
    path("api/logout", LogoutUser.as_view(), name="logout"),
    path("api/likes/", CreateLikeView.as_view(), name="add_users_likes"),
    path(
        "api/likes/user-likes", GetUserLikes.as_view(), name="get_user_likes"
    ),
    path("api/", include("Comments.urls")),
    path("api/", include("Notifications.urls")),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
