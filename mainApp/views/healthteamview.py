from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def health_team(request):

    healthteam = HealthTeam.objects.all();

    context = {
        'health_team': healthteam
    }
    return render(request, 'mainApp/health_team.html',context)


def health_team_profile(request,pk):
    try:
        team_member = HealthTeam.objects.get(pk=pk)
    except:
        return redirect('home')

    context = {
        'team_member': team_member
    }
    return render(request, 'mainApp/health_team_profile.html',context)

    