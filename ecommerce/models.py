from django.db import models


class Product (models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    stock = models.IntegerField()


class Order (models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    date_time = models.DateField(auto_now=True) #Registra el update


class OrderDetail (models.Model):
    order = models.ForeignKey(Order, related_name='details', on_delete=models.CASCADE)
    cuantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
