from django.shortcuts import render, HttpResponse

from django.template import loader
# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def room1(request):
    return render(request, 'room1.html', {})
def room2(request):
    return render(request, 'room2.html', {})
def room3(request):
    return render(request, 'room3.html', {})