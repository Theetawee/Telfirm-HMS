from datetime import date
import random
import string
from django.db import models
from django.dispatch import receiver
from accounts.models import Department, MedicalWorker
from django.db.models.signals import post_save
from patients.utils import GENDER_CHOICES, RESULTS_FAST, STATUS_CHOICES, WARD

# Create your models here.


class Test(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    
    
    @property
    def has_results(self,patient):
        if Result.objects.filter(test=self,patient=patient).exists():
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

    
    

    @property
    def has_results(self,patient):
        if Result.objects.filter(test=self,patient=patient).exists():
            return True
        else:
            return False
    
    
    def __str__(self):
        return self.name




class Result(models.Model):
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

        


