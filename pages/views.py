from django.shortcuts import render, HttpResponse
from .models import Product, Category
# Create your views here.


def home_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/index.html", context)


def shop_view(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        "products": products
    }
    return render(request, "pages/shop.html", context)

"""
1. asdas
2. eqwqw
3. eqweq
"""

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    images = product.productimage_set.all()
    context = {
        "product": product,
        "images": enumerate(images),
        "images2": images,
    }
    return render(request, "pages/detail.html", context)