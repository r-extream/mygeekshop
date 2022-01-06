import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from mainapp.models import ProductCategory, Product


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    return render(request, 'mainapp/products.html', {'links_menu': links_menu})


def contact(request):
    with open('contacts.json') as input_file:
        contacts = json.load(input_file)
    return render(request, 'mainapp/contact.html', {'contacts': contacts})

