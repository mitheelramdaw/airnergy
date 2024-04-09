from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1> home page</h1>")

def about(response):
    return HttpResponse("<h1> about page </h1>")

def contact(response):
    return HttpResponse("<h1> contact page </h1>")