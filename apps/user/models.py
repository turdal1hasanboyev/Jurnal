from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser
from ckeditor.fields import RichTextField
from datetime import date
import re
from ..common.models import BaseModel


class CustomUserManager(UserManager):
    def create_user(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not phone_number:
            raise ValueError('Users must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Users must have a valid phone number')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')
        if not password:
            raise ValueError('Users must have a password')
        
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, phone_number, first_name, last_name, password=None, **extra_fields):
        # extra_fields.setdefault('is_staff', True)
        # extra_fields.setdefault('is_superuser', True)

        ## extra_fields.update({'is_staff': True, 'is_superuser': True})

        # if extra_fields.get('is_staff') is not True:
        #     raise ValueError('Superuser must have is_staff=True.')
        # if extra_fields.get('is_superuser') is not True:
        #     raise ValueError('Superuser must have is_superuser=True.')

        if not email:
            raise ValueError('Superusers must have an email address')
        if not phone_number:
            raise ValueError('Superusers must have a phone number')
        if not re.match(r'^\+?[0-9]{10,15}$', phone_number):
            raise ValueError('Superusers must have a valid phone number')
        if not first_name:
            raise ValueError('Superusers must have a first name')
        if not last_name:
            raise ValueError('Superusers must have a last name')
        if not password:
            raise ValueError('Superusers must have a password')
        
        user = self.create_user(email=email, phone_number=phone_number, first_name=first_name, last_name=last_name, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractUser, BaseModel):
    GENDER = (
        ('Ayol', ('Ayol')),
        ('Erkak', ('Erkak')),
    )
    username = None
    email = models.EmailField(unique=True)
    description = RichTextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', default='img/default.png')
    video = models.FileField(upload_to='videos')
    gender = models.CharField(max_length=10, choices=GENDER)
    adress = RichTextField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'phone_number',
        'first_name',
        'last_name',
        ]

    def __str__(self):
        if self.get_full_name():
            return f"{self.get_full_name()}"
        return f"{self.email}"
    
    def age(self):
        if not isinstance(self.birth_date, date):
            return None
        today = date.today()
        age = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            age -= 1
        return age
    
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"