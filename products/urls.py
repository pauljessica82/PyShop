from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('new', views.new_product),
    path('cart', views.cart),
    path('checkout', views.checkout),

]
