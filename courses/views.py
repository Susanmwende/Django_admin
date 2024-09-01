from django.shortcuts import render
from .forms import CoursesRegistrationForm

def register_courses(request):
    form=CoursesRegistrationForm()
    return render(request,"courses/register_courses.html",{"form":form})

