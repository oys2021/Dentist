from multiprocessing import context
from re import template
from django.shortcuts import render
from django.views.generic import View
from Fit.models import Appoint,Patient,Doctor,Profile,visit


class IndexView(View):
    template_name="dashboard/index.html"

    def get(self,request,*args, **kwargs):
        context={
            "appoint":Appoint.objects.all(),
            "patient":Patient.objects.all(),
            "doctor":Doctor.objects.all(),
            "visit":visit.objects.all()
        }
        return render(request,self.template_name,context)

