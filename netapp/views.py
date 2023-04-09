from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Nerecords, PErecords


# Create your views here.
def home(request):
    disp_nerecords = Nerecords.objects.all()

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
            return render(request,'home.html',{'nerecords':disp_nerecords})
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
def pes(request):
    if request.user.is_authenticated:
        disp_perecords = PErecords.objects.all()
        return render(request,'pes.html',{'perecords':disp_perecords})
    else:
        return redirect('login')

