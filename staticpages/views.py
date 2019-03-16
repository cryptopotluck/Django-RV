from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'staticpages/index.html')

def gallary(request):
    return render(request,'staticpages/gallary.html')

def aboutus(request):
    return render(request, 'staticpages/aboutus.html')