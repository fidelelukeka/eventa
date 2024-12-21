from tkinter import CASCADE
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 255)
    userlastname = models.CharField(max_length = 255)
    adresse = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    telephone = models.CharField(max_length = 255)