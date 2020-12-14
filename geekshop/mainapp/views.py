from django.shortcuts import render

from mainapp.models import Product, ProductCategory


def main(request):
    content = {
        'title': 'GeekShop - Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request, id=None):
    content = {
        'title': 'GeekShop - Категории',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'mainapp/products.html', content)
