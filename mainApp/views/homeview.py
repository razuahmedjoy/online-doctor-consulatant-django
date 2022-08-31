from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *
def home(request):
    context = {}

    doctors = Doctor.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = Faq.objects.all()
    clients = Clients.objects.all()

    context['doctors'] = doctors
    context['testimonials'] = testimonials
    context['faqs'] = faqs
    context['clients'] = clients


    return render(request, 'mainApp/home.html',context)


def doctor_public_profile(request,pk):
    context = {}
    try:
        doctor =Doctor.objects.get(pk=pk)
    except:
        return redirect('home')
    context['doctor'] = doctor
    return render(request, 'mainApp/doctor_profile.html',context)