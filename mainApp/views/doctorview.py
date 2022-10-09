from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from mainApp.models import *
from .checkuserrole import *
from .forms import doctorProfileForm
import json




@login_required(login_url="/login/")
@user_passes_test(is_doctor,login_url="/")
def doctor_dashboard(request):

    doctor = get_doctor(request.user)

    appointments = Appointment.objects.filter(doctor=doctor).order_by('-created_at')
    pending_appointments = appointments.filter(status="Pending").count()
    approved_appointments = appointments.filter(status="Approved").count()

    context = {
        "doctor":doctor,
        "appointments":appointments,
        "pending_appointments":pending_appointments,
        "approved_appointments":approved_appointments
    }

    return render(request,"doctor/dashboard.html",context)


@login_required(login_url="/login/")
@user_passes_test(is_doctor,login_url="/")
def doctor_profile(request):
    
    return render(request,"doctor/profile.html")



@login_required(login_url="/login/")
@user_passes_test(is_doctor,login_url="/")
def doctor_profile_update(request):

    context = {}
    doctor = get_doctor(request.user)

    form = doctorProfileForm(instance=doctor)

    if request.method == "POST":
        formData = doctorProfileForm(request.POST,request.FILES,instance=doctor)
        if formData.is_valid():
            formData.save()
            return redirect('doctor_profile')


    context["form"] = form

    return render(request,"doctor/update_profile.html",context)




@login_required(login_url="/login/")
@user_passes_test(is_doctor,login_url="/")
def doctor_appointment_details(request,pk):

    context = {}

    try:
        appointment = Appointment.objects.get(pk=pk)
        doctor = get_doctor(request.user)
        if doctor.id != appointment.doctor.id:
            return HttpResponse("No Access")
    except:
        return redirect('home')

    if request.method == "POST":
        medicineNames = request.POST.getlist("medicineName")
        measure = request.POST.getlist("measure")
        comment = request.POST.get("comment")
        updatePrescription = int(request.POST.get("updatePrescription"))


        if updatePrescription:
       
            prescription = Prescription.objects.get(pk=updatePrescription)
            medicines = []
            for i in range(len(medicineNames)):
                item = {
                    "medicine":medicineNames[i],
                    "measure":measure[i],
                }
                medicines.append(item)
            medicines = json.dumps(medicines)
            prescription.medicines=medicines
            prescription.comment=comment
            prescription.save()

            
        else:
            medicines = []
            for i in range(len(medicineNames)):
                item = {
                    "medicine":medicineNames[i],
                    "measure":measure[i],
                }
                medicines.append(item)
            medicines = json.dumps(medicines)
            prescription = Prescription(appointment=appointment,medicines=medicines,comment=comment)
            prescription.save()
            appointment.status = "Approved"
            appointment.save()
   
            
        
    
   
    
    context["appointment"] = appointment
    try: 
        prescription = appointment.prescription
      
        context["prescription"] = prescription
        context["medicines"] = json.loads(prescription.medicines)
    except:
        pass

    return render(request,"doctor/doctor_appointment_details.html",context)
  

    
