from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(request):
    return render(request, 'home.html', {'name': 'Rajesh'})

def predictByName(request):
    return render(request, 'predictByName.html')

def predictByHeight(request):
    return render(request, 'predictByHeight.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def faq(request):
    return render(request, 'faq.html')
