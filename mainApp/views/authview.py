from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import Group

from .checkuserrole import *

def register(request):
    if request.user.is_authenticated:
        return redirect("/")
    error = ""
    context = {
        "title":"Create Your Account",
        "error": error
    }
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        contact_no = request.POST.get('contact_no')
        gender = request.POST.get('gender')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')
        
        
        try:
            exist = User.objects.get(username=contact_no)
            context["error"] = "Already have a Account with this number"
        except:
            userModel = User.objects.create_user(username=contact_no,password=password1,first_name=full_name)
            userModel.save()

            if role == "patient": 
                patient = Patient(user=userModel,full_name=full_name,contact_no=contact_no,gender=gender,role=role)
                patient.save()
                patient_group = Group.objects.get_or_create(name='PATIENT')
                patient_group[0].user_set.add(userModel)

            elif role == "doctor":
                doctor = Doctor(user=userModel,full_name=full_name,contact_no=contact_no,gender=gender,role=role)
                doctor.save()
                doctor_group = Group.objects.get_or_create(name='DOCTOR')
                doctor_group[0].user_set.add(userModel)


            return redirect("/login?accountCreated=1")
                
            


    return render(request,"mainApp/register.html",context)


# login view

def login_view(request):

    if request.user.is_authenticated:
        return redirect("/")

    error = ""
    context = {
        "title":"Login",
        "error": error
    }
    if request.GET.get("accountCreated"):
        context["registration_done"] = "Your account created Successfully, Login Now"
    if request.method == "POST":
        context["registration_done"] = ""
        contact_no = request.POST.get("contact_no")
        password = request.POST.get('password')

        user = authenticate(request,username=contact_no,password=password)

        if user is not None:
            login(request,user)
         
            if "next" in request.GET:
                return redirect(request.GET["next"])
            
            if is_doctor(request.user):
                return redirect("doctor_dashboard")
            elif is_patient(request.user):
                return redirect("patient_dashboard")

        else:
            context["error"] = "Invalid Contact no or Password"
            



    return render(request,"mainApp/login.html",context)

# logout view

def logout_view(request):
    logout(request)
    return redirect("home")