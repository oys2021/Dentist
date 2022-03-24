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