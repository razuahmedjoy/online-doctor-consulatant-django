from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *
def home(request):
    context = {}

    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    clients = Clients.objects.all()
    sliders = Slider.objects.all()
    counters = Counter.objects.all()
    web_setting = Web_Settings.objects.last()
    village_care_centers = Village_Care_Center.objects.all()




    consultants = doctors.filter(type='Consultant')[0:4]
    telemedicine = doctors.filter(type='Telemedicine')[0:4]
    ruralDoctors = doctors.filter(type='Rural')[0:4]
    # print(consultants)
    context['consultants'] = consultants
    context['telemedicine'] = telemedicine
    context['ruralDoctors'] = ruralDoctors
    
    context['testimonials'] = testimonials
    context['faqs'] = faqs
    context['clients'] = clients
    context['sliders'] = sliders
    context['counters'] = counters
    context['web_setting'] = web_setting
    context['village_care_centers'] = village_care_centers
  


    return render(request, 'mainApp/home.html',context)


def doctor_public_profile(request,pk):
    context = {}
    try:
        doctor =Doctor.objects.get(pk=pk)
    except:
        return redirect('home')
    context['doctor'] = doctor
    return render(request, 'mainApp/doctor_profile.html',context)


def all_doctors(request,type):
    context = {}
    try:
        doctors = Doctor.objects.filter(type=type)
    except:
        return redirect('home')
    context['doctors'] = doctors
    return render(request, 'mainApp/all_doctor.html',context)