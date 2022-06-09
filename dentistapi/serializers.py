from django.db.models import fields
from rest_framework import serializers
from Fit.models import *


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"

class DentistSerializer(serializers.ModelSerializer):
    class Meta:
        model=Dentist
        fields="__all__"

