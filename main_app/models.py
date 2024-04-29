from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Candy(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    cost = models.IntegerField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candies = models.ManyToManyField(Candy, through='OrderItems')

class OrderItems(models.Model):
    order = models.ForeignKey(Order)
    candy = models.ForeignKey(Candy)
    quantity = models.IntegerField()