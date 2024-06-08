# crypto/models.py

from django.db import models

class Coin(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    market_cap = models.BigIntegerField()
    price = models.FloatField()

    def __str__(self):
        return self.name
