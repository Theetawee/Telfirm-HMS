from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from .utils import (
    SPECIALIZATION_CHOICES,
    OTHER,
    GENDER_CHOICES,
    STATUS_CHOICES,
    WARD,
    RESULTS_FAST
)
import random
import string
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date





class AccountManager(BaseUserManager):
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        if not name:
            raise ValueError('The Name field must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, name, password, **extra_fields)





class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MedicalWorker(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    phone = PhoneNumberField(null=True,blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='Date joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='Last login')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(null=True,blank=True,max_length=300)
    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES,
        default=OTHER,
    )
    license_number = models.CharField(max_length=20, blank=True)
    department = models.ForeignKey(
        "Department", on_delete=models.SET_NULL, null=True, blank=True
    )

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = AccountManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def has_module_perms(self, app_label):
        return True






class Test(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    
    @property
    def has_results(self,patient):
        if Results.objects.filter(test=self,patient=patient).exists():
            return True
        else:
            return False
    
    

    @property
    def has_results(self,patient):
        if Results.objects.filter(test=self,patient=patient).exists():
            return True
        else:
            return False
    
    
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

    tests = models.ManyToManyField(Test, blank=True,related_name='tests')

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
        ordering = ["-id"]


class Results(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    results = models.CharField(
        null=True,
        blank=True,
        choices=RESULTS_FAST,
        max_length=100,
        verbose_name="Test result",
    )
    comment = models.TextField(null=True, blank=True, verbose_name="Comment")
    date = models.DateTimeField(blank=True, null=True)
    done_by = models.ForeignKey(
        MedicalWorker, on_delete=models.SET_NULL, null=True, blank=True
    )
    done = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.name}'s results -{self.test.name}"


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

        # Create result entries for each test associated with the patient
        for test in instance.tests.all():
            Results.objects.create(patient=instance,tea=test, test=test,done=False).save()












