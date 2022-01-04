from django.http.response import HttpResponse
from django.shortcuts import render

def get_clinics(request):
    context = {}
    return render(request, 'base.html', context)

def get_shops(request):
    context = {}
    return render(request, 'base.html', context)

def get_areas(request):
    context = {}
    return render(request, 'base.html', context)