from tkinter import Widget
from turtle import textinput
from django import forms
from django.forms import TextInput
from  Fit.models import *
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude=[
        "gender",
        "id",
        "phone"
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

class DentistForm(forms.ModelForm):
    class Meta:
        model = Dentist
        exclude=[
        "id",
        "gender",
        "phone_number"
        ]
        widgets={
          'dentist_name':TextInput(attrs={
              'class':"form-control",
              'style':'max-width:300px',
              'placeholder':'name'

            }),
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

        




  


        