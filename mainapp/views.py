import json

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import ProductCategory, Product


def index(request):
    return render(request, 'mainapp/index.html')


def products(request, pk=None):
    links_menu = ProductCategory.objects.all()
    if pk is not None:
        if pk == 0:
            category_item = {'name': 'Все', 'pk': 0}
            products_list = Product.objects.all()
        else:
            category_item = get_object_or_404(ProductCategory, pk=pk)
            products_list = Product.objects.filter(category__pk=pk)

        context = {
            'links_menu': links_menu,
            'products': products_list,
            'category': category_item,
            'basket': Basket.objects.filter(user=request.user)
        }
        return render(request, 'mainapp/products_list.html', context)

    context = {
        'links_menu': links_menu,
        'title': 'Товары',
        'hot_product': Product.objects.all().first(),
        'same_products': Product.objects.all()[3:5],
        'basket': Basket.objects.filter(user=request.user)
    }
    return render(request, 'mainapp/products.html', context)


def contact(request):
    with open('contacts.json') as input_file:
        contacts = json.load(input_file)
    return render(request, 'mainapp/contact.html', {'contacts': contacts})

