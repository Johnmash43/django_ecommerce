from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name="home"),
    path('shop',shop, name="shop"),
    path('contact',contact, name="contact"),
    path( 'about',about, name="about"),
    path('contact/form/submit',submitContactForm, name="contact.form"),
    path('form/success',successRedirect, name="contact.redirect"),
]