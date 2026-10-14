from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("home")
def contactus(request):
    return HttpResponse("contact")
def aboutus(request):
    return HttpResponse("about")