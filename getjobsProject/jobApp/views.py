from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hydjobs(request):
    s = '<h1>Hyderabad Jobs Information</h1>'
    return HttpResponse(s)
def mumjobs(request):
    s = 'Mumbai Jobs Information'
    return HttpResponse(s)
def deljobs(request):
    s = 'Delhi Jobs Information'
    return HttpResponse(s)
def banjobs(request):
    s = 'Banglore Jobs Information'
    return HttpResponse(s)
def rajjobs(request):
    s = 'Rajasthan Jobs Information'
    return HttpResponse(s)
