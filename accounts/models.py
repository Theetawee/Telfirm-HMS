from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from .utils import (
    SPECIALIZATION_CHOICES,
    OTHER,
    GENDER_CHOICES,
    STATUS_CHOICES,
    WARD,
    MICROBIOLOGY_TESTS_CHOICES,
    PARASITOLOGY_TESTS_CHOICES,
    IMMUNOLOGY_TESTS_CHOICES,
    CHEMISTRY_TESTS_CHOICES,
    HAEMATOLOGY_TESTS_CHOICES,
)
import random
import string
from django.dispatch import receiver
from django.db.models.signals import post_save
from multiselectfield import MultiSelectField
from datetime import date


class MedicalWorker(AbstractUser):
    phone = PhoneNumberField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES,
        default=OTHER,
    )
    email = models.EmailField(unique=True)
    license_number = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(
        "Department", on_delete=models.SET_NULL, null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return self.username


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Test(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    
    def __str__(self):
        return self.name

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    medical_record_number = models.CharField(max_length=20, unique=True)
    admission_date = models.DateTimeField(auto_now_add=True)
    discharge_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    ward = models.CharField(max_length=3, choices=WARD)

    allergies = models.TextField(blank=True, null=True)
    current_medications = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)

    emergency_contact_name = models.CharField(max_length=100, blank=True, null=True)
    emergency_contact_number = models.CharField(max_length=15, blank=True, null=True)

    comments = models.TextField(blank=True, null=True)

    tests = models.ManyToManyField(Test, blank=True)



    def __str__(self):
        return f"{self.first_name} {self.last_name} (MRN: {self.medical_record_number})"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def age(self):
        today = date.today()
        delta = today - self.date_of_birth
        age_years = delta.days // 365
        return max(age_years, 0)

    class Meta:
        ordering=['-id']

@receiver(post_save, sender=Patient)
def assign_mrn(sender, instance, created, **kwargs):
    if created:
        while True:
            # Generate a new MRN
            initials = "".join(random.choices(string.ascii_uppercase, k=3))
            digits = "".join(random.choices(string.digits, k=9))
            new_mrn = f"P-{digits}{initials}"

            # Check if the generated MRN already exists
            if not Patient.objects.filter(medical_record_number=new_mrn).exists():
                instance.medical_record_number = new_mrn
                instance.save()
                break
