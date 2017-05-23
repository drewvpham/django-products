from django.shortcuts import render, redirect
from .models import Product

# Create your views here.
def index(request):
    b=Product.objects.create(name='Burrito', description='its got beans and meats', weight='3', price='12', cost='10', category='Mehican')
    a=Product.objects.create(name='Apple', description='its an apple', weight='3', price='12', cost='10', category='fruit')
    c=Product.objects.create(name='chicken head', description='its a chicken head', weight='3', price='12', cost='10', category='gross')
    print a.name
    return render(request, 'products/index.html')
