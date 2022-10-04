from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def medicine_bank(request):


    return render(request, 'mainApp/medicine_bank.html',context={})
