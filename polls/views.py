from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def aboutPage(request):
    return HttpResponse('<h1>This is about page</h1>')