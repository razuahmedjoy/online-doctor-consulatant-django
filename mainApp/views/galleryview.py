from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def all_gallery(request):
    context = {}

    gallery = Gallery.objects.all()

    context["gallery"] = gallery


    return render(request, 'mainApp/gallery.html',context)

