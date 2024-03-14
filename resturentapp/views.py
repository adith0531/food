from django.shortcuts import render
from resturentapp .models import *
from userapp.models import *


# Create your views here.
def salrestruant(request):
    return render(request,'saltrestruant.html')
