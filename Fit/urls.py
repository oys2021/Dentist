from django.urls import path
from .import views
from django.urls import path
from .import views 


urlpatterns=[
path("home",views.home,name="home"),
path("about",views.about,name="about"),
path("contact",views.contact,name="contact"),
path("blog_single",views.blog_single,name="single"),
path("blog",views.blog,name="blog"),
path("doctors",views.doctors,name="doctors"),
path("services",views.services,name="services"),
path("login",views.login,name="login"),
path("signup",views.signup,name="signup"),
path("recover",views.recover_password,name="recover"),
path("logout",views.logout,name="logout"),
path("administration",views.admin,name="admin"),
] 