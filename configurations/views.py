from django.shortcuts import render
from django.http import HttpResponse

def accueil(request):
    return HttpResponse('accueil')

def pageA(request):
    return HttpResponse('pageA')

def pageB(request):
    return HttpResponse('pageB')

def pageC(request):
    return HttpResponse('pageC')
# Create your views here.
