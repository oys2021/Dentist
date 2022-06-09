from django.urls import path
from .import views 
urlpatterns = [
	path("patientlist",views.patientlist,name="patientlist"),
    path("createpatient",views.createpatient,name="createpatient"),
    path("patientdetails/<int:pk>",views.patientdetails,name="patientdetails"),
    path("updatepatient",views.updatepatient,name="updatepatient"),
    path("deletepatient",views.deletepatient,name="deletepatient"),
    path("Dentistlist",views.Dentistlist,name="Dentistlist"),
    path("Dentistdetails",views.Dentistdetails,name="Dentistdetails"),
    path("updateDentist",views.updateDentist,name="updateDentist"),
    path("createDentist",views.createDentist,name="createDentist"),
    path("deleteDentist",views.deleteDentist,name="deleteDentist"),

]
