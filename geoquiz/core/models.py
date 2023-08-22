"""
Database models.
"""
# import uuid
# import os

# from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Level(models.Model):
    """Model representing a level in the game."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
        """
        method to provide a human-readable representation
        of the level when it is displayed in the Django
        admin or in other contexts.
        """


class Categories(models.Model):
    """Model representing a category."""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Challenges(models.Model):
    name = models.CharField(max_length=255)
    difficulty = models.IntegerField(null=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE, null=False)
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, null=False)
    photo_link = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class CapitalName(models.Model):
    country_name = models.CharField(max_length=100)
    capital_name = models.CharField(max_length=100)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.country_name
