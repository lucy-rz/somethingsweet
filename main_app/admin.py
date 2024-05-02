from django.contrib import admin
from .models import Candy, Order, OrderItem, Photo

# Register your models here.
admin.site.register(Candy)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Photo)
