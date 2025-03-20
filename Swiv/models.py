# Create your models here.
from django.db import models
from django import forms

# Create your models here.
class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models. PositiveIntegerField()
    persons  =models.IntegerField()
    date = models.DateField((""), auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return f'{self.name} {self.email} {self.number} {self.persons} {self.date}'
    