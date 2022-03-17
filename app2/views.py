from urllib import response
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def csk(request):
    return HttpResponse('csk fan')
def mum(request):
    return HttpResponse('mum fans')
