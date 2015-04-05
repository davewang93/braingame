from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("David says hey there world!")
