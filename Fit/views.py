from unicodedata import name
from urllib import request
from django.shortcuts import render
from django.http import response
from django.contrib.auth.models import auth,User
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import  Appoint, Dentist,UserProfile
from Fit.forms import AppointmentForm,ProfileForm
from django.views.generic import View
from django.contrib import messages    
from django.core.mail import send_mail   
from django.conf import settings as conf_settings
   
def home(request):
    dentist=Dentist.objects.all()
    context={"dentist":dentist}
    return render(request,"Fit/spindex.html",context)


class AppointmentView(View):
    template_name='Fit/appointment.html'
    form_class=AppointmentForm
    def get(self,request,*args, **kwargs):
        context={"form":AppointmentForm}
        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        prof=request.user
        form=AppointmentForm(request.POST,instance=prof)
        if form.is_valid():
            form.save()
        return redirect("home")




def contact(request):
    return render(request,"Fit/contact.html",{})

    
  

def about(request):
    return render(request,"Fit/about.html",{})

def Dentists(request):
    dentist=Dentist.objects.all()
    context={"dentist":dentist}
    return render(request,"Fit/Dentists.html",context)

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



    
class Profile(View):
    template_name="Fit/userprofile.html"
    form_class=ProfileForm
    model_class=UserProfile
  


    def get(self,request,*args, **kwargs):
        context={"forms":ProfileForm}
        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        prof=request.user
        form=ProfileForm(request.POST,request.FILES,instance=prof)
        if form.is_valid():
            form.save()
            return redirect("profile")
        else:
            return HttpResponse('<h1>Page not found</h1>')

       
       
	
	
