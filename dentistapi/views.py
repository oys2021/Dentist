from pickle import GET
from django.shortcuts import render
from Fit.models import Patient,Dentist
from django.contrib.auth.models import auth,User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from dentistapi.serializers import PatientSerializer,DentistSerializer


# Create your views here.

@api_view(['GET'])
def patientlist(request):
    patient=Patient.objects.all()
    serializer=PatientSerializer(patient,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createpatient(request):
    prof=request.user
    serializer=PatientSerializer(data=request.data,instance=prof)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def patientdetails(request,pk):
    patient=Dentist.objects.get(id=pk)
    serializer=PatientSerializer(patient,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updatepatient(request,pk):
    patient=Patient.objects.get(id=pk)
    serializer=PatientSerializer(instance=patient,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def deletepatient(request,pk):
    patient=Patient.objects.get(id=pk)
    patient.delete()

# Doctoer View

@api_view(['GET'])
def Dentistlist(request):
    Dentist=Dentist.objects.all()
    serializer=DentistSerializer(Dentist,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createDentist(request):
    serializer=DentistSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def Dentistdetails(request,pk):
    Dentist=Dentist.objects.get(id=pk)
    serializer=DentistSerializer(Dentist,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def updateDentist(request,pk):
    Dentist=Dentist.objects.get(id=pk)
    serializer=DentistSerializer(instance=Dentist,data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def deleteDentist(request,pk):
    Dentist=Dentist.objects.get(id=pk)
    Dentist.delete()







