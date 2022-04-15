import email
from unicodedata import name
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
# Foreign keys help you to migrate entities using a primary key from the parent table.
# A foreign key enables you to link two or more tables together.
# ......
# Each patient and doctor and admin is a user
# patient and profile is one to one so as doctors
class Appoint(models.Model):
    patient_name=models.CharField(max_length=100,null=True)
    doctor_name=models.CharField(max_length=100,null=True)  
    email=models.CharField(max_length=100,null=True)
    message=models.CharField(max_length=500,null=True)



class Patient(models.Model):
    patient_name=models.ForeignKey(Appoint,on_delete=models.CASCADE,null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=5,null=True)
    address=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=100,null=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)

class Doctor(models.Model):
    doctor_name=models.ForeignKey(Appoint,on_delete=models.CASCADE,null=True)
    age=models.IntegerField(null=True)
    gender=models.CharField(max_length=5,null=True)
    address=models.CharField(max_length=100,null=True)
    phone_number=models.CharField(max_length=100,null=True)


    

class Profile(models.Model):
    # picture=models.ImageField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=100)

class visit(models.Model):
    diagnosis=models.CharField(max_length=100,null=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,null=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,null=True)
    appointment=models.ForeignKey(Appoint,on_delete=models.CASCADE,null=True)
    prescription=models.CharField(max_length=100,null=True)

# class ContactInfo(models.Model)


    



# https://data-flair.training/blogs/django-rest-framework/
# list
# create
# retrieve (pk needed)
# update (pk needed)
# partial_update (pk needed)
# destroy (pk needed)


#next- payment and visit model
