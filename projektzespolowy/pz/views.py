from django.shortcuts import render

def store(request):
    context = {}
    return render(request, 'pz/store.html', context)

def cart(request):
    context = {}
    return render(request, 'pz/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'pz/checkout.html', context)
