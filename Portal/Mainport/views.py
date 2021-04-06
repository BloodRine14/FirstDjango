from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'home.html')
    # return HttpResponse("This is mainpage of the portal")

def about(request):
    return HttpResponse("This is about page of the portal")

def catalogue(request):
    return HttpResponse("This is catalogue page")

def showcase(request):
    return HttpResponse("This is showcase page")
