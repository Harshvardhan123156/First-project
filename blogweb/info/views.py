from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("hey this if the infrmation section.")

def about(request):
    return HttpResponse("it is all about us for now.")

def contact(request):
    return HttpResponse("contact us for further quesries")

# Create your views here.
