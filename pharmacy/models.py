from django.db import models
from patients.models import Patient
# Create your models here.


class Drug(models.Model):
    name=models.CharField(max_length=200)
    stock=models.PositiveIntegerField()
    used=models.PositiveIntegerField(default=0)
    expiry_date=models.DateField(null=True,blank=True)
    price_number=models.DecimalField(decimal_places=2,default=100,max_digits=100000000)
    
    def __str__(self):
        return self.name
    
    
    
class Prescription(models.Model):
    drugs=models.ManyToManyField(Drug,blank=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    detail=models.TextField(null=True,blank=True)
    def __str__(self):
        return f'Prescription for {self.patient.name}'