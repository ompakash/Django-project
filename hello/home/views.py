from django.shortcuts import render,HttpResponse
# Create your views here.


def index(request):
    return render(request,'index.html')

def service(request):
    return HttpResponse("This is Service Page ")

def about(request):
    return HttpResponse("This is About Page ")

def contact(request):
    return HttpResponse("This is Contact Page ")