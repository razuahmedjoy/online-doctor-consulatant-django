from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def about_us(request):
    context={}

    about = About.objects.last()
    about_team = AboutTeam.objects.all()

    context["about"] = about
    context["about_team"] = about_team

    return render(request, 'mainApp/about_us.html',context)
