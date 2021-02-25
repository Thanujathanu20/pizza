from django.db import models

# Create your models here.

class PizzaModel(models.Model):
    pizzaType = models.CharField('Pizza Type', max_length=100)
    pizzaSize = models.CharField(max_length=100)
    toppings = models.CharField(max_length=100)


    def __str__(self):
        return self.pizzaType