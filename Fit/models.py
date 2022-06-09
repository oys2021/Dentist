import email
from email.policy import default
from unicodedata import name
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL






class Patient(models.Model):
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=5,null=True)
    address=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

class Dentist(models.Model):
    dentist_name=models.CharField(max_length=100,null=True) 
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=5,null=True)
    address=models.CharField(max_length=100,null=True)
    image=models.ImageField(null=True,blank=True,upload_to="images/")

class Appoint(models.Model):
    email=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    message=models.CharField(max_length=500,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    

class UserProfile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic=models.ImageField(null=True,blank=True)

class DentistProfile(models.Model):
    dentist=models.OneToOneField(Dentist,on_delete=models.CASCADE,null=True)
    
class visit(models.Model):
    diagnosis=models.CharField(max_length=100,null=True)
    dentist=models.ForeignKey(Dentist,on_delete=models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    appointment=models.ForeignKey(Appoint,on_delete=models.CASCADE,null=True)
    prescription=models.CharField(max_length=100,null=True)

