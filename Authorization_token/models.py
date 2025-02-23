import random
import string
import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models



def generate_random_username(length=10):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_username = ''.join(random.choices(characters, k=length))
    return random_username


class AuthorizationUserOnTokenManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Создает и сохраняет пользователя с введенным им email и паролем.
        """
        if not username:
            raise ValueError('username должен быть указан')
        username = self.normalize_email(username)
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)

    def get_by_natural_key(self, username):
        return self.get(username=username)


class AuthorizationUserOnToken(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    username = models.CharField(max_length=150, blank=True, unique=True, default=generate_random_username())
    email = models.EmailField(max_length=254, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    changed = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)

    objects = AuthorizationUserOnTokenManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class TokenForRegistration(models.Model):
    user = models.OneToOneField(AuthorizationUserOnToken, on_delete=models.SET_NULL, null=True)
    telegram_username = models.CharField(max_length=255, default='name')
    chat_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    registration_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
