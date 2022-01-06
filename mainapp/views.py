import json

from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


links_menu = [
    {'category_link': 'super_sport', 'category_name': 'super sport'},
    {'category_link': 'street', 'category_name': 'street'},
    {'category_link': 'cruisers', 'category_name': 'cruisers'},
    {'category_link': 'touring', 'category_name': 'touring'},
    {'category_link': 'adventure', 'category_name': 'adventure'},
]


def products(request, category=None):
    return render(request, 'mainapp/products.html', {'links_menu': links_menu})


def contact(request):
    with open('contacts.json') as input_file:
        contacts = json.load(input_file)
    return render(request, 'mainapp/contact.html', {'contacts': contacts})