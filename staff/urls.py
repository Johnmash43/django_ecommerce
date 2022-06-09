from django.urls import path
from .views import *

urlpatterns = [

    path("dashboard", dashboard, name="dashboard"),
    path("categories", categories, name="categories"),
    path("products", products, name="products"),
]