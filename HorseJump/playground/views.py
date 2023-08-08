# from ml-code.horse_height import horse_height
from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
from django.http import JsonResponse
from .ml_code.horse_height import horse_height
# import sys


# Loading a method from horse_height.py
# sys.path.insert(0, 'HorseJump/playground/ml-code')
hh = horse_height()

# Loading the ML Model
model_height = load("/workspaces/Horse-Breeding-App/HorseJump/playground/ml_code/savedModels/model_by_height.joblib")

# Create your views here.

def homePage(request):
    return render(request, 'home.html', {'name': 'Vishal'})

def predictByName(request):
    return render(request, 'predictByName.html', {"male":hh.male_horse_height, "female":hh.female_horse_height })

def predictByHeight(request):
    return render(request, 'predictByHeight.html')

def aboutUs(request):
    return render(request, 'aboutUs.html')

def faq(request):
    return render(request, 'faq.html')

def predict_by_height(request):
    sire_height = float(request.GET['sire_height'])
    dam_height = float(request.GET['dam_height'])
    pred = model_height.predict([[sire_height, dam_height]])
    print(sire_height)
    print(dam_height)
    data = {'predicted_value': pred[0]}
    return JsonResponse(data)

def predict_by_name(request):
    hh.male_horse_height
    hh.female_horse_height