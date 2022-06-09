from django.urls import path
from .import views
from django.urls import path
from .import views 


urlpatterns=[
path("home",views.home,name="home"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact"),
path("dentists",views.Dentists,name="dentists"),
path("services",views.services,name="services"),
path("login",views.login,name="login"),
path("signup",views.signup,name="signup"),
path("recover",views.recover_password,name="recover"),
path("logout",views.logout,name="logout"),
path("administration",views.admin,name="admin"),
path("appointment",views.AppointmentView.as_view(),name="appointment"),
path("userprofile/<str:username>",views.Profile.as_view(),name="profile"),
] 