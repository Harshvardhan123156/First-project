from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("hey this if the infrmation section.")

def about(request):
    return render(request , 'info/about.html')

def contact(request):
    if request.method=='POST':
        print("we are using post")
    return render(request , 'info/contact.html')

# Create your views here.
