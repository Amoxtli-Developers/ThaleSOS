from django.db import models

# Create your models here.

class Adverts(models.Model):
    id = models.AutoField(primary_key=True)
    words = models.CharField(max_length=100)
    category = models.ForeignKey('Categories', on_delete=models.CASCADE)

class Categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

