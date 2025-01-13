from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    stock = models.IntegerField()