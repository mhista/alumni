from distutils.command.upload import upload
from django.db import models
from .image_check import passport_uploads,business_uploads
# Create your models here.

class Alumni(models.Model):
    firstname = models.CharField(max_length=30)
    surname =  models.CharField(max_length=30)
    othernames =  models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    year_of_graduation =  models.CharField(max_length=4)
    discipline =  models.CharField(max_length=30)
    passport = models.ImageField(upload_to=passport_uploads)
    subscribed = models.BooleanField(default=False)
    company_name = models.CharField(max_length=50,blank=True,null=True)
    nature_of_biz = models.TextField(blank=True,null=True)
    bussines_photo = models.ImageField(upload_to=passport_uploads,blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.firstname} {self.surname}"
    
