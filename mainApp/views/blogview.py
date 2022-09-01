from django.shortcuts import render,HttpResponse,redirect
from mainApp.models import *

def all_blog(request):
    context = {}

    blogs = Blog.objects.all()

    context["blogs"] = blogs


    return render(request, 'mainApp/all_blog.html',context)

def single_blog(request,id):
    context = {}

    try:
        single_blog = Blog.objects.get(pk=id)
        context["single_blog"] = single_blog
    except:
        return redirect('all_blog')

    return render(request, 'mainApp/single_blog.html',context)
