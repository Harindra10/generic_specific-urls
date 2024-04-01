from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kallempudi(request):
    return HttpResponse('kallempudi is the best village comper to based villages')