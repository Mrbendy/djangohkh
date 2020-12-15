from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello,world')

def index(request):
    return render(request, 'base.html')


def remodel(request):
    return render(request, 'model.html')