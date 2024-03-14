from django.shortcuts import render
from .models import *
from adminapp .models import *
from resturentapp.models import *

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')
def cart(request):
    return render(request,'cart.html')
def help(request):
    return render(request,'help.html')

def biriyani(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'biriyani.html', {'data': data})

def burger(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'burger.html', {'data': data})

def shawarma(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'shawarma.html', {'data': data})

def desert(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'desert.html', {'data': data})

def pizza(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'piza.html', {'data': data})

def drinks(request):
    data=Subcategorymodel.objects.all()
    for item in data:
        item.star_rating = range(item.Rating) if item.Rating is not None else None
    return render(request, 'drinks.html', {'data': data})

def wishlist(request):
    return render(request, 'wishlist.html')

def profile(request):
    return render(request, 'profile.html')


