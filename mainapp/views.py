import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, CatalogCategory


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def main(request):
    content = {
        'title': 'Главная'
    }
    return render(request, 'mainapp/index.html', content)


def catalog(request, pk=None, page=1):

    title = 'товары'
    links_menu = CatalogCategory.objects.all()

    if pk is not None:
        if pk == 0:
            category = {'pk': 0, 'name': 'все'}
            products = Product.objects.all().order_by('price')

        else:
            category = get_object_or_404(CatalogCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_product()
    same_products = get_same_products(hot_product)

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'hot_product': hot_product
    }

    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    content = {
        'title': 'Контакты'
    }
    return render(request, 'mainapp/contacts.html', content)


def games(request):
    content = {
        'title': 'Игры'
    }
    return render(request, 'mainapp/games.html', content)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': CatalogCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk)
    }

    return render(request, 'mainapp/product.html', content)


def product_1(request):
    content = {
        'title': 'Schecter Demon-7'
    }
    return render(request, 'mainapp/catalog/product_1.html', content)


def product_2(request):
    context = {
        'title': 'Schecter OMEN-8',
    }
    return render(request, 'mainapp/catalog/product_2.html', context)


def product_3(request):
    context = {
        'title': 'Schecter C-5 BASS SGR',
    }
    return render(request, 'mainapp/catalog/product_3.html', context)
