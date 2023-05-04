from django.urls import path
from . import views

"""
{% url 'main:home' %}
{% url 'pages:home' %}
"""
app_name = "main"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("shop/", views.shop_view, name="shop"),
    path("shop/categories/<slug:slug>/", views.category_products, name="category_products"),
    path("shop/products/<slug:slug>/", views.product_detail, name="product_detail")
]
