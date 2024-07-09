from django.shortcuts import render
from.models import *
# Create your views here.

def home(request): 
    items = Item.objects.all()
    #context = {"item_element" :items}
    #thejshtesi
    context = {"items": items}
    return render(request, 'home.html', context)

def about(request): 
    return render(request,"about.html")
