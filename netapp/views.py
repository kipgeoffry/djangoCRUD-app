from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('home')
        else:
            messages.success(request, "Login Failed!,Invalid username or password")
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return render(request,'home.html',{})
        else:
            return redirect('login')
# def userAuth(request):
#     #  check to see if user has supplied correct cerentials
#         if request.method == 'POST':
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                login(request,user)
#                messages.success(request,"Login successful")
#                return redirect('home')
#             else:
#                messages.success(request, "Login Failed,Please try again...")
#                return redirect('login')
          
def userLogin(request):
    return render(request,'login.html',{})

def userLogout(request):
    logout(request)
    messages.success(request, "Logged out...")
    return redirect('home')
