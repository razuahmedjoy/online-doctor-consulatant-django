from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def medicine_bank(request):
    web_setting = Web_Settings.objects.last()

    context = {
        "web_setting":web_setting
    }


    return render(request, 'mainApp/medicine_bank.html',context)
