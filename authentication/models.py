from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, name, email, password=None):
        if email is None:
            raise TypeError('El correo no se ha ingresado')
            
        username = email
        user = self.model(username=username, name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password=None, name='admin'):
        if password is None:
            raise TypeError('La contraseña no se ha ingresado')

        if email is None:
            raise TypeError('El correo no se ha ingresado')
            
        username = email
        user = self.model(username=username, name=name, email=self.normalize_email(email))
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.is_verified = True
        user.is_active = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    name = models.CharField(max_length=200)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.email

    # JWT
    def tokens(self):
        jwt_token = RefreshToken.for_user(self)
        return {
            'refresh': str(jwt_token),
            'access': str(jwt_token.access_token)
        }
