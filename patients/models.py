from datetime import date
from django.db import models
from accounts.models import MedicalWorker, Department
from pharmacy.models import Prescription

# Create your models here.


class Test(models.Model):
    TEST_TYPES=(("R", "Rapid"), ("S", "Standard"))
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    units=models.CharField(max_length=20,blank=True,null=True)
    test_type=models.CharField(max_length=20,choices=TEST_TYPES,default="R")
    @property
    def has_results(self, patient):
        if Result.objects.filter(test=self, patient=patient).exists():
            return True
        else:
            return False

    def __str__(self):
        return self.name


class Patient(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    )
    STATUS_CHOICES = (
        ("A", "Admitted"),
        ("D", "Discharged"),
        ("O", "Other"),
    )
    WARD = (("OPD", "OPD"), ("IPD", "IPD"))

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)

    mrn = models.CharField(
        max_length=20, unique=True, verbose_name="Medical Record Number"
    )
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

    tests = models.ManyToManyField(Test, blank=True, related_name="tests")

    prescription = models.ForeignKey(
        Prescription, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} (MRN: {self.mrn})"

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
    def undone_tests(self):
        if Result.objects.filter(patient=self,confirmed=False).exists():
            return True
        
        
        
    def __str__(self):
        return self.name


class Result(models.Model):
    RAPID_TEST_RESULTS = (("P", "POSTIVE"), ("N", "NEGATIVE"))

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    rapid_tr = models.CharField(
        null=True,
        blank=True,
        choices=RAPID_TEST_RESULTS,
        max_length=100,
        verbose_name="Rapid Test result",
    )
    standard_tr=models.TextField(null=True,blank=True,verbose_name="Standard Test results")
    comment = models.TextField(null=True, blank=True, verbose_name="Comment")
    date = models.DateTimeField(blank=True, null=True)
    done_by = models.ForeignKey(
        MedicalWorker, on_delete=models.SET_NULL, null=True, blank=True
    )
    done = models.BooleanField(default=False)
    confirmed=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.patient.name}'s results -{self.test.name}"

    class Meta:
        ordering=['done','confirmed']