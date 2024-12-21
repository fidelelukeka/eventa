from tkinter import CASCADE
from django.db import models

# Create your models here.

class Event(models.Model):
    category = models.ForeignKey('category.Category', on_delete=models.CASCADE)
    titre = models.CharField(max_length = 255)
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    is_free = models.BooleanField(default = 1)
    price = price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add = True)
    lieu = models.CharField(max_length = 255)
