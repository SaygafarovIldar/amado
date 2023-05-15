from django.urls import path

from . import views


# http://127.0.0.1:8000
urlpatterns = [
    path("", views.cart_view, name="cart"),
    path("checkout/", views.checkout_view, name="checkout")
]
