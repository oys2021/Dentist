from django.urls import path
from .import views
from django.urls import path
from .import views 


urlpatterns=[
path("",views.home,name="home"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact"),
path("blog_single",views.blog_single,name="single"),
path("blog",views.blog,name="blog"),
path("doctors",views.doctors,name="doctors"),
path("services",views.services,name="services"),
] 