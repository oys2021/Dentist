from django.shortcuts import render
from django.http import response
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect


# Create your views here.
def home(request):
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
            return redirect("/")
        else:
            print("BYE")

    else:
        return render(request,"Fit/login.html",{})


def signup(request):
    if request.method=="POST":
        first_name=request.POST["first"]
        last_name=request.POST["last"]
        username=request.POST["user"]
        password1=request.POST["p1"]
        password2=request.POST["p2"]
        email=request.POST["email"]

        if password1==password2:
             user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
             user.save()
             return redirect("/")
        else:
            print("Error")

    else:
        return render(request,"Fit/signup.html",{})
