from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .utils import SPECIALIZATION_CHOICES,OTHER


class MedicalWorker(AbstractUser):
    phone = PhoneNumberField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES,
        default=OTHER,
    )
    license_number = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
