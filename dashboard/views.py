from multiprocessing import context
from re import template
from tkinter import PhotoImage
from typing import _ProtocolMeta
from django.shortcuts import render,redirect,get_object_or_404,HttpResponseRedirect
from django.views.generic import View
from dashboard.forms import PatientForm,DentistForm
from Fit.models import Appoint,Patient,Dentist
from django.contrib.auth.models import auth,User
from django.http import HttpResponse



class PatientView(View):
    template_name="dashboard/patient.html"

    def get(self,request,*args, **kwargs):
        context={
            "Patient":Patient.objects.all()
        }
        return render(request,self.template_name,context)

class DentistView(View):
    template_name="dashboard/Dentist.html"

    def get(self,request,*args, **kwargs):
        context={"Dentist":Dentist.objects.all() }
        return render(request,self.template_name,context)

class VisitView(View):
    template_name="dashboard/View.html"

    def get(self,request,*args, **kwargs):
        context={"Dentist":Dentist.objects.all() }
        return render(request,self.template_name,context)

class CreatePatientView(View):
    template_name="dashboard/createPatient.html"
    form_class=PatientForm
    model_class=Patient



    def get(self,request,*args, **kwargs):
        context={"createPatient":Patient.objects.all(),"form":PatientForm}
        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request.META.get("HTTP_REFERER"))
        





class PatientDetailView(View):
    template_name="dashboard/patientdetails.html"
    model_class=Patient

    def get(self,request,*args, **kwargs):
        patient = Patient.objects.get(id=kwargs['pk'])
        context={"Patient":patient}
        return render(request,self.template_name,context)


class UpdatePatientView(View):
    template_name="dashboard/updatepatient.html"
    form_class=PatientForm

    def get(self,request,*args, **kwargs):
        context={"forming":PatientForm}
        return render(request,self.template_name,context)
    

    def post(self,request,*args, **kwargs):
        patient= get_object_or_404(Patient, id =kwargs['pk'])
        form =PatientForm(request.POST or None,instance=patient)
        if form.is_valid():
            form.save()
            return redirect("dashboard:patient")

class DeletePatientView(View):
    template_name="dashboard/deletepatient.html"

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        delete= Patient.objects.get(id=kwargs['pk'])
        delete.delete()
        return redirect("dashboard:patient")


class CreateDentistView(View):
    template_name="dashboard/createDentist.html"
    form_class=DentistForm
    model_class=Dentist 


    def get(self,request,*args, **kwargs):
        context={"createDentist":Dentist.objects.all(),"forms":DentistForm}
        return render(request,self.template_name,context)
    
    def post(self,request,*args, **kwargs):
        form=DentistForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(request.META.get("HTTP_REFERER"))
        

class DentistDetailView(View):
    template_name="dashboard/Dentistdetails.html"

    def get(self,request,*args, **kwargs):
        dentist=Dentist.objects.get(id=kwargs['pk'])
        context={"Dentist":dentist}
        return render(request,self.template_name,context)

class UpdateDentistView(View):
    template_name="dashboard/updateDentist.html"
    form_class=DentistForm

    def get(self,request,*args, **kwargs):
        context={"forming":DentistForm}
        return render(request,self.template_name,context)
    

    def post(self,request,*args, **kwargs):
        Dentist= get_object_or_404(Dentist, id =kwargs['pk'])
        form =DentistForm(request.POST or None,instance=Dentist)
        if form.is_valid():
            form.save()
            return redirect("dashboard:Dentist")

class DeleteDentistView(View):
    template_name="dashboard/deleteDentist.html"

    def get(self,request,*args, **kwargs):
        return render(request,self.template_name)

    def post(self, request, *args, **kwargs):
        delete= Dentist.objects.get(id=kwargs['pk'])
        delete.delete()
        return redirect("dashboard:Dentist")

    
       

           
        
        










       



        








