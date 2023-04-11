from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from netapp.models import Nerecords, PErecords
from netapp.forms import AddNeForm


# Create your views here.
def home(request): 
    if request.user.is_authenticated:
        disp_nerecords = Nerecords.objects.all()
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
def ne_record(request,pk): 
    if request.user.is_authenticated:
        #Lookup for record on DB pass record primary key and assign details to variable ne_details
        ne_details = Nerecords.objects.get(id=pk)
        #render the record details on html document,passing details as nedetails
        return render(request,'nedetails.html',{'nedetails':ne_details})
    else:
        return redirect('login')
    
def pe(request):
    if request.user.is_authenticated:
        return render(request,'pe.html',{})
    else:
        return redirect('login')
def delete_nerecord(request,pk):
    if request.user.is_authenticated:
        delete_ne = Nerecords.objects.get(id=pk)
        delete_ne.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        return redirect('login')

def add_ne(request):
    addNeForm = AddNeForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if addNeForm.is_valid():
                # add_ne_details = addNeForm.save()
                addNeForm.save()
                messages.success(request, "NE added Successfully")
                return redirect('home')
            messages.success(request, "Form Invalid")              
        return render(request,'add_ne.html',{"form":addNeForm})
    else:
        return redirect('login')

def update_nerecord(request,pk):
    current_record = Nerecords.objects.get(id=pk)
    updateform = AddNeForm(request.POST or None,instance=current_record)
    if request.user.is_authenticated:
        # when user is POSTING,
        if updateform.is_valid():
            updateform.save()
            messages.success(request, "NE Updated Successfully")
            return redirect('home')
        #IF user is not posting i.e when None,display the form
        return render(request,'update_ne.html',{"upform":updateform})

    else:
        return redirect('login')