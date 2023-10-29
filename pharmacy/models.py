from django.db import models
# Create your models here.


class Drug(models.Model):
    name=models.CharField(max_length=200)
    stock=models.PositiveIntegerField()
    used=models.PositiveIntegerField(default=0)
    expiry_date=models.DateField(null=True,blank=True)
    price_number=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
    
    
    
class Prescription(models.Model):
    drugs=models.ManyToManyField(Drug,blank=True)
    def __str__(self):
        return f'Prescription {self.pk}'