from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def first(request):
    return HttpResponse('<h1>Dhruba_Sundar</h1>')
def second(request):
    return HttpResponse('<h1>Mechanical Engineer</h1>')