from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Customer(User):

    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name       

class Product(models.Model):

    LIVE = 0
    OUT_OF_STOCK = 1
    PENDING = 2

    PRODUCT_STATUS =(
        (LIVE,"Live"),
        (OUT_OF_STOCK, "Out of stock"),
        (PENDING, "Pending"),
    )

    name = models.TextField()
    price = models.FloatField()
    description = models.TextField()
    status = models.IntegerField(choices=PRODUCT_STATUS,default=LIVE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, blank=True)
    quantity = models.IntegerField()    
    image = models.ImageField(null=True, blank=True)  

    def __str__(self):
        return self.name


class Review(models.Model):

    ratings = models.IntegerField()
    feedback = models.TextField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

class Order(models.Model):

    total = models.FloatField()
    order_number = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer.username


class CartProduct(models.Model):

    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Payment(models.Model):

    CASH = 0
    MPESA = 1

    PAYMENT_STATUS =(
        (CASH,"Cash"),
        (MPESA,"M-pesa")
    )

    method = models.IntegerField(choices=PAYMENT_STATUS,default=MPESA)
    total = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    description = models.CharField(max_length=30, null=True, blank=True)
    reference_number = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reference_number


    
    


    
