from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class NewUserManager(BaseUserManager):
    """Custom user manager."""
    def create_user(self, **kwargs):
        """Create a user."""
        email = kwargs.get("email")
        password = kwargs.get("password")
        if not email:
            raise ValueError("Users must have an email")

        user = self.model(
            email=self.normalize_email(email),
            first_name=kwargs.get("first_name", ""),
            last_name=kwargs.get("last_name", ""),
            phone_number=kwargs.get("phone_number")
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, **kwargs):
        return self.create_user(**kwargs)


class NewUser(AbstractBaseUser):
    """AbstractBaseUser only contains the authentication functionality,
    but no actual fields: you have to supply them when you subclass"""
    USERNAME_FIELD = "email"
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True, blank=False)
    phone_number = models.IntegerField(null=True)
    password = models.CharField(max_length=200)

    objects = NewUserManager()

    class Meta:
        ordering = ['-id']



