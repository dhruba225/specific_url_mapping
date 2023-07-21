from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>I Know Python and SQL</h1>')
def second(request):
    return HttpResponse("<h1>I Am A Django Developer</h1>")