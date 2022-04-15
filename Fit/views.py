from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import response
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import  Appoint, Doctor, Patient
from django.conf import settings
User = settings.AUTH_USER_MODEL

from django.contrib import messages
# Create your views here.
# def home(request):
#    
#        
#        
#        
#        

#          appoint=Appointment.objects.create()
        
       
#        

       
        

        
       
#        
    
#     else:
#        
   
def home(request):
    if request.method=="POST":
        name=request.POST["names"]
        doctor=request.POST["doctor"]
        email=request.POST["emails"]
        messages=request.POST["info"]
        
     
       
    


        
        user=Appoint.objects.create(patient_name=name,email=email,doctor_name=doctor,message=messages)
        user.save()
        return redirect("services")

    else:
        return render(request,"Fit/spindex.html",{})


           
    
    
   



   

# def test(request):
#     return render(request,"Fit/test.html",{})

def blog(request):
    return render(request,"Fit/blog.html",{})

def contact(request):
    
    return render(request,"Fit/contact.html",{})

def about(request):
    return render(request,"Fit/about.html",{})

def doctors(request):
    return render(request,"Fit/doctors.html",{})

def blog_single(request):
    return render(request,"Fit/blog-single.html",{})

def services(request):
    return render(request,"Fit/services.html",{})


def login(request):
    if request.method=="POST":
        username=request.POST["user"]
        password=request.POST["pass"]

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            print("BYE")

    else:
        return render(request,"Fit/login.html",{})


def signup(request):
    if request.method=="POST":
        first_name=request.POST["first"]
        last_name=request.POST["second"]
        username=request.POST["user"]
        password1=request.POST["p1"]
        password2=request.POST["p2"]
        email=request.POST["email"]

        if password1==password2:
            user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
            user.save()
            return redirect("login")
        else:
            print("Error")

    else:
        return render(request,"Fit/signup.html",{})

def recover_password(request):
    if request.method=="POST":
        username=request.POST["user"]
        new_password=request.POST["password1"]
        confirm_password=request.POST["password2"]

        if new_password==confirm_password:
            u=User.objects.get(username=username)
            u.set_password(new_password)
            u.save()
            user=auth.authenticate(username=username,password=new_password)
            auth.login(request,user)
            return redirect("home")
        else:
            return  messages.warning(request, 'Your account expires in three days.')
        
    return render(request,"Fit/recover.html",{})

def logout(request):
    auth.logout(request)
    return redirect("home")

def Appointment(request):
    return render(request,"Fit/")

def admin(request):
    return render(request,"Fit/admin.html",{})

       
       
	
	
