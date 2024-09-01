from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)  
            return redirect("homepage")  
        else:
            messages.error(request, "Invalid username or password")
    
    return render(request, 'accounts/login.html')

def user_logout(request):
    logout(request)
    return redirect("login")  
