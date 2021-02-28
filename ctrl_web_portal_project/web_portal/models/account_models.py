from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from web_portal.models.company_models import CompanyModel


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Creates and saves a new super user"""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        user = self.create_user(email, password, **extra_fields)
        user.save(using=self._db)
        return user


class AccountModel(AbstractBaseUser, PermissionsMixin):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    username = None
    password = models.CharField(
        max_length=50,
        default='root123'
    )
    email = models.EmailField(
        'email address',
        unique=True
    )
    company = models.ForeignKey(
        CompanyModel,
        on_delete=models.CASCADE,
        related_name='users',
        null=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.firstname} + {self.lastname} + {self.id}"

    class Meta:
        db_table = "accounts_db"
