from django.shortcuts import render


def main(request):
    content = {
        'title': 'GeekShop - Главная'
    }
    return render(request, 'mainapp/index.html', content)


def products(request):
    content = {
        'title': 'GeekShop - Категории'
    }
    return render(request, 'mainapp/products.html', content)


def test_context(request):
    """Test function for getting acquainted with the context."""
    context = {
        'title': 'Test Context',
        'header': 'Добро пожловать на сайт!',
        'username': 'Герман Триг',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '6 090,00 руб.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.'},
        ],
        'promotion': True,
        'products_of_promotion': [
            {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.'},
        ]
    }
    return render(request, 'mainapp/test_context.html', context)