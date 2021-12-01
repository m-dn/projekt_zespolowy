from django.shortcuts import render
from .models import *


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'pz/store.html', context)


def cart(request):
    context = {}
    return render(request, 'pz/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'pz/checkout.html', context)
