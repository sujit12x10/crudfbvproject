from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    s = '<h1> Hello Welcome to Django Classes. Well Done TONI</h1>'
    return HttpResponse(s)

# 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