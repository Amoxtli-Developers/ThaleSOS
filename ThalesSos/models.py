from django.db import models

# Create your models here.

class Warning(models.Model):
    id = models.AutoField(primary_key=True)
    keywords = models.CharField(max_length=100)
    category = models.ForeignKey('Categorie', on_delete=models.CASCADE)

class Categorie(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

