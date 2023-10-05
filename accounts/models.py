from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.conf import settings
import os
# Create your models here.


class Account(AbstractUser):
    phone=PhoneNumberField(null=True,blank=True)
    profile_image=models.ImageField(upload_to='profiles/',null=True,blank=True)
    
    # Set the email field as the USERNAME_FIELD for authentication
    USERNAME_FIELD = 'username'
    # Add 'email' to the REQUIRED_FIELDS for the createsuperuser command
    REQUIRED_FIELDS = ['email','first_name','last_name']

    def __str__(self):
        return self.username

    @property
    def image(self):
        if self.profile_image:
            return self.profile_image.url
        else:
            url=os.path.join(settings.STATIC_URL,'images','default.webp')
            return url

