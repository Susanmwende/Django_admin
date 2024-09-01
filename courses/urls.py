from django.urls import path
from .import  views



urlpatterns = [
    path("register/",views.register_courses, name="register_courses")
]