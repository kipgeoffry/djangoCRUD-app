from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from netapp.models import Nerecords, PErecords
from netapp.forms import AddNeForm, AddPeForm


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
#This is a function to display List of PEs
def pes(request):
    if request.user.is_authenticated:
        disp_perecords = PErecords.objects.all()
        return render(request,'pes.html',{'perecords':disp_perecords})
    else:
        return redirect('login')
    
    # function to view individual NE record
def ne_record(request,pk): 
    if request.user.is_authenticated:
        #Lookup for record on DB pass record primary key and assign details to variable ne_details
        ne_details = Nerecords.objects.get(id=pk)
        #render the record details on html document,passing details as nedetails
        return render(request,'nedetails.html',{'nedetails':ne_details})
    else:
        return redirect('login')
 # example function for testing purposes   
def pe(request):
    if request.user.is_authenticated:
        return render(request,'pe.html',{})
    else:
        return redirect('login')
# A funtion to delete NE record
def delete_nerecord(request,pk):
    if request.user.is_authenticated:
        delete_ne = Nerecords.objects.get(id=pk)
        delete_ne.delete()
        messages.success(request, "Record Deleted Successfully")
        return redirect('home')
    else:
        return redirect('login')
# A function do add NE record
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
    
#A function to update NE record
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
    
# A function to add PE record
def add_pe(request):
    addPeFom = AddPeForm(request.POST or None)
    if request.user.is_authenticated:
        #when a post request is received,first check if form is valid if valid save the form
        #if not POSTng,just display the form i.e user can be posting or viewing the form
        if request.method == "POST":
            if addPeFom.is_valid():
                addPeFom.save()
                messages.success(request, "PE added Successfully")
                return redirect('pes')
            # messages.success(request, "Form Invalid")              
        return render(request,'add_pe.html',{"addform":addPeFom})
    else:
        return redirect('login')

#This funtion updates PE information
def update_pe(request,pk):
    current_pe = PErecords.objects.get(id=pk)
    updatePeform = AddPeForm(request.POST or None,instance=current_pe)
    if request.user.is_authenticated:
        if request.method == "POST":
            if updatePeform.is_valid():
                updatePeform.save()
                messages.success(request, "PE Updated Successfully")
                return redirect('pes')
        #IF user is not posting i.e when None,display the form
        return render(request,'update_pe.html',{"upPeForm":updatePeform})

    else:
        return redirect('login')
    
#This is a funtion that deletes PE,it gets a request with Primary KEY
def delete_pe(request,pk):
    if request.user.is_authenticated:
        delete_pe = PErecords.objects.get(id=pk)
        delete_pe.delete()
        messages.success(request, "PE Deleted Successfully")
        return redirect('pes')
    else:
        return redirect('login')
