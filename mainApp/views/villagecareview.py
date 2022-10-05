from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def single_village_care(request,pk):

    context = {}

    try:
        village_care = Village_Care_Center.objects.get(pk=pk)
        context["village_care"] = village_care
    except:
        return redirect('home')

    return render(request, 'mainApp/single_village_care.html',context)
