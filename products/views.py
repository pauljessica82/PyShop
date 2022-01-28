from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def cart(request):
    context = {}
    return render(request, "cart.html")


def checkout(request):
    context = {}
    return render(request, "checkout.html")


def index(request):
    products = Product.objects.all()
    return render(request, "store.html", {'products': products})


def new_product(request):
    return HttpResponse('New product')
