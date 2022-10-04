from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def health_team(request):

    healthteam = HealthTeam.objects.all();

    context = {
        'health_team': healthteam
    }
    return render(request, 'mainApp/health_team.html',context)