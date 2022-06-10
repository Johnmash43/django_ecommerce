from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from .models import *

# Create your views here.

def home(request):

    context = {}
    return render(request, "index.html",context)

def contact(request):

    context = {}
    return render(request, "contact.html",context)
      
def about(request):

    context = {}
    return render (request, "about.html", context)


def shop(request):
    context = {
        "product": product
    }
    return render (request, "shop.html",context)

def product(request):

    context = {}
    return render (request, "product.html", context)    


def submitContactForm(request):

    if request.method == "POST":
       
       form_data = request.POST
       email = form_data["email"]
       name = form_data["name"]
       number = form_dat["number"]
       message = form_data["message"]


       return HttpResponseRedirect("/form/success")
    
    else:
        return HttpResponseRedirect("/")  
  

def successRedirect(request):

    context = {}
    return render (request, "success.html", context)


def ajaxContactSubmission(request):

    email= request.POST["email"]
    name= request.POST["name"]
    number= request.POST["number"]
    message = request.POST["message"]

    context={
        "success": True,
        "message": "Message saved successfully"
    }

    return JsonResponse(context)


def getProductDetails(request, id):

    try:
        product = Product.objects.get(pk=id)
    except Product.DoesNotExist:

        messages.info("Sorry, that product does not exist")
        return HttpResponseRedirect("/")

    categories =Category.objects.all()
    all_products = Product.objects.exclude(pk=id)

    context = {
        "product":product,
        "categories": categories,
        "more_products": all_products
    }

    return render(request, "product-details.html", context) 

def searchProducts(request):

    query = request.POST["query"]

    products = Product.objects.filter(
        status = Product.LIVE).filter(name__contains=query)
        

    context = {
        "products": products
    } 

    return render(request, "shop.html", context) 

def cart(request):

    cart = Product.objects.all()

    context = {
        "product": product
    }    

    return render(request,"add-to-cart.html", context)


