from django.db import models

# Create your models here.


class Drug(models.Model):
    name=models.CharField(max_length=200)
    stock=models.PositiveIntegerField()
    used=models.PositiveIntegerField()
    expiry_date=models.DateField()
    price_number=models.DecimalField(decimal_places=2,max_digits=100000000)
    
    def __str__(self):
        return self.name