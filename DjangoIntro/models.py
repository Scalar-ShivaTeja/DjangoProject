from django.db import models

class User(models.Model):
    TITLE_CHOICES = [
        ('Mr', 'Mr'),
        ('Ms', 'Ms'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
    ]
    username = models.CharField(max_length=20)
    title = models.CharField(max_length=5, choices=TITLE_CHOICES)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    seller = models.ForeignKey('User', on_delete=models.CASCADE, null=True)
    description = models.TextField()
    stock = models.IntegerField()
