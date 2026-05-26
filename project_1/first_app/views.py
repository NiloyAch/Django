from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
   ## return HttpResponse("this is first app page")

# def courses(request):
  #  return HttpResponse("this is courses page")
 # def about(request):
   # return HttpResponse("This is first app/about page")
    return render(request,'first_app/home.html')