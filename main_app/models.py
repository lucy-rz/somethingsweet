from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Candy(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    cost = models.IntegerField()

    def __str__(self):
        return f'name:{self.name} candy_id:{self.id} cost:{self.cost}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'candy_id': self.id})

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    candies = models.ManyToManyField(Candy, through='OrderItem')
    current_order = models.BooleanField(default=True)

    def __str__(self):
        return f'order: {self.user_id} {self.current_order}'

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'order_id:{self.order_id} candy_id:{self.candy_id} qty:{self.quantity}'
    
class Photo(models.Model):
    url = models.CharField(max_length=300)
    candy = models.ForeignKey(Candy, on_delete=models.CASCADE)
    def __str__(self):
      return f'{self.candy_id} @{self.url}'
