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

    consultants = doctors.filter(type='Consultant')
    telemedicine = doctors.filter(type='Telemedicine')
    ruralDoctors = doctors.filter(type='Rural')

    context['consultants'] = consultants
    context['telemedicine'] = telemedicine
    context['ruralDoctors'] = ruralDoctors
    
    context['testimonials'] = testimonials
    context['faqs'] = faqs
    context['clients'] = clients
    context['sliders'] = sliders
    context['counters'] = counters
    


    return render(request, 'mainApp/home.html',context)


def doctor_public_profile(request,pk):
    context = {}
    try:
        doctor =Doctor.objects.get(pk=pk)
    except:
        return redirect('home')
    context['doctor'] = doctor
    return render(request, 'mainApp/doctor_profile.html',context)