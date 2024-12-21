from django.db import models

# Create your models here.

class Ticket(models.Model):
    event = models.ForeignKey('event.Event', on_delete=models.CASCADE)
    owner = models.CharField(max_length = 255)
    
