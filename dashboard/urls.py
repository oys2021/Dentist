from django.urls import path
from . import views

app_name = "dashboard"

urlpatterns = [
    path("patient", views.PatientView.as_view(), name="patient"),
    path("Dentist", views.DentistView.as_view(), name="Dentist"),
    path("visit", views.VisitView.as_view(), name="visit"),
    path("createPatient", views.CreatePatientView.as_view(), name="createPatient"),
    path("createDentist", views.CreateDentistView.as_view(), name="createDentist"),
    path("dentistdetails/<int:pk>", views.DentistDetailView.as_view(), name="dentist"),
    path("updateDentist/<int:pk>",views.UpdateDentistView.as_view(), name="updateDentist"),
    path("deleteDentist/<int:pk>",views.DeleteDentistView.as_view(), name="deleteDentist"),
    path("patientdetails/<int:pk>", views.PatientDetailView.as_view(), name="pat"),
    path("updatepatient/<int:pk>",views.UpdatePatientView.as_view(), name="updatepatient"),
    path("deletepatient/<int:pk>",views.DeletePatientView.as_view(), name="deletepatient"),



]

