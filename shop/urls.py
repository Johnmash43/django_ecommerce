from django.urls import path
from .views import home,contact, about, shop

urlpatterns = [
    path('',home, name="home"),
    path('shop',shop, name="shop"),
    path('contact',contact, name="contact"),
    path( 'about',about, name="about"),
]