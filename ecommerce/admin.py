from django.contrib import admin
from ecommerce.models import Product
from ecommerce.models import Order
from ecommerce.models import OrderDetail

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderDetail)


