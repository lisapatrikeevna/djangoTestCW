# Create your views here.

# myapp/views.py
from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    return HttpResponse("<h1>Hello, from fox!</h1>")


def first_view(request):
    return render(request, 'foxApp/index.html', {})


def contacts_view(request):
    return render(request, 'foxApp/contacts.html', {})
