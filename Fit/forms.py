from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import TextInput,Textarea
from  Fit.models import *


    
class AppointmentForm(forms.ModelForm):
    class Meta:
        model =Appoint

        exclude=[
        "id",
        "user"
        ]
        
        widgets={
            'email':TextInput(attrs={
              'class':"form-control",
              'style':'max-width:300px',
              'placeholder':'email'

            }),
          'message':Textarea(attrs={
              'class':"form-control",
              'style':'max-width:300px', 
              'placeholder':'Symptoms'
            

}),

 
            
        }
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude=[
        "user",
        "id",
        "gender"
        ]
        
        widgets={
            'age':TextInput(attrs={
              'class':"form-control",
              'style':'max-width:300px',
              'placeholder':'Age'

            }),
          'address':TextInput(attrs={
              'class':"form-control",
              'style':'max-width:300px', 
              'placeholder':'address'

            }),
             'phone_number':TextInput(attrs={
              'class':"form-control",
              'style':'max-width:300px',
              'placeholder':'phone_number'

}),
 
            
        }
        
    
     
        
   
 


 
            
     

        




  


        