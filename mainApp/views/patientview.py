
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from mainApp.models import *
from .checkuserrole import *
import json 
@login_required(login_url="/login/")
@user_passes_test(is_patient,login_url="/")
def patient_dashboard(request):

    patient = get_patient(request.user)

    appointments = Appointment.objects.filter(patient=patient).order_by('-created_at')
    pending_appointments = appointments.filter(status="Pending").count()
    approved_appointments = appointments.filter(status="Approved").count()

    context = {
        "patient":patient,
        "appointments":appointments,
        "pending_appointments":pending_appointments,
        "approved_appointments":approved_appointments
    }

    return render(request,"patient/dashboard.html",context)



@login_required(login_url="/login/")
@user_passes_test(is_patient,login_url="/")
def patient_new_appointment(request):
    context = {}
    doctors = Doctor.objects.all()
    context["doctors"] = doctors
    # print(doctors)
    
    return render(request,"patient/new_appointment.html",context)


@login_required(login_url="/login/")
@user_passes_test(is_patient,login_url="/")
def patient_submit_new_appointment(request,pk):
    context = {}
    if request.method == "POST":
        doctorid = request.POST.get("doctor")
        patientid = request.POST.get("patient")
        description = request.POST.get("description")
        appointment_date = request.POST.get("date")
        print(appointment_date)
        doctor = Doctor.objects.get(pk=doctorid)
        patient = Patient.objects.get(pk=patientid)

        # create appointment
        appointment = Appointment(patient=patient,doctor=doctor, description=description,appointment_date=appointment_date)
        appointment.save()

        return redirect('patient_dashboard')

    try:
        doctor = Doctor.objects.get(pk=pk)
        context["doctor"] = doctor
    except:
        return redirect('/')
    
    
    return render(request,"patient/appointment_form.html",context)


@login_required(login_url="/login/")
@user_passes_test(is_patient,login_url="/")
def patient_profile(request):
    
    return render(request,"patient/profile.html")

def doctor_dashboard(request):
    return HttpResponse("doctor Dashboard")




@login_required(login_url="/login/")
@user_passes_test(is_patient,login_url="/")

def patient_appointment_details(request,pk):

    context = {}

    try:
        appointment = Appointment.objects.get(pk=pk)
        patient = get_patient(request.user)
        if patient.id != appointment.patient.id:
            return HttpResponse("No Access")
    except:
        return redirect('home')

    if request.method == "POST":
       return HttpResponse("Bad request")
   
            
        
    
   
    
    context["appointment"] = appointment
    try: 
        prescription = appointment.prescription
      
        context["prescription"] = prescription
        context["medicines"] = json.loads(prescription.medicines)
    except:
        print("No prescription")

    return render(request,"patient/patient_appointment_details.html",context)
  