from django.db import models


class Laptops(models.Model):
    model = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)
    ram = models.IntegerField()
    ssd = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField()
