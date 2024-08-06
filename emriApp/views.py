from django.shortcuts import render
from.models import *
from django.contrib import messages
# Create your views here.

def home(request): 
    categories = Category.objects.all()
    items = Item.objects.all()
    #context = {"item_element" :items}
    #thejshtesi
    context = {"items": items,  "categories" : categories}
    return render(request, 'home.html', context)

def about(request): 
    categories = Category.objects.all()
    context = {"categories" : categories}
    return render(request,"about.html", context)

def detailitem(request, id):
    categories = Category.objects.all()
    itemDetail= Item.objects.get(pk=id)
    context = {"itemDetail": itemDetail,  "categories" : categories,}
    return render(request,  'detailitem.html', context)


def detailCategory(request, slug):
    categories = Category.objects.all()
    categoryDetail= Category.objects.get(category_slug=slug)
    categoryItems=Item.objects.filter(item_category=categoryDetail)
    context = {"categoryDetail": categoryDetail, "categories" : categories,  "categoryItems": categoryItems}
    return render(request,  'detailCategory.html', context)

def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST["firstName"]
        surname = request.POST["lastName"]
        email= request.POST["email"]
        comment = request.POST["comment"]
        if name !="" and surname !="" and email !="" and comment != "":
            Contact(
            contact_name = name,
            contact_surname = surname,
            contact_email = email,
            contact_description = comment
        ).save()
            messages.success(request, 'Message sended!!!')
        else:
            messages.error(request, 'Message not sended!!!')
        Contact(
            contact_name = name,
            contact_surname = surname,
            contact_email = email,
            contact_description = comment
        ).save()
        
        
    context = {"categories":categories}
    return render(request,  'contact.html', context)
