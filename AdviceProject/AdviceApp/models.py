from django.db import models
from django.utils import timezone

# Create your models here.
class EntryItem(models.Model):
    title = models.CharField(max_length=200)
    entry = models.CharField(max_length=1000)

class Advice(models.Model):
    advice = models.CharField(max_length=1000)