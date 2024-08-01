from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    #return HttpResponse('<h1> Hola soy Juan Camilo </h1>')
    #return render(request,'home.html')
    return render(request,'home.html',{'name':' Juan Camilo '})
def about(request):
    #return HttpResponse('<h2>Welcome to ABOUT page</h2>')
    return render(request,'about.html')
