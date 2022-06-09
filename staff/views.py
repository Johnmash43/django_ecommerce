from django.shortcuts import render

# Create your views here.


def dashboard(request):

    context = {}

    return render(request,"dashboard.html",context)

def categories(request):

    categories = Category.objects.all()

    context = {
        "categories".categories
    }

    return render(request,"category.html",context)


def products(request):

    context = {}

    return render(request, "product.html",context)