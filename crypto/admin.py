# crypto/admin.py

from django.contrib import admin
from .models import Coin

@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol', 'market_cap', 'price')
    search_fields = ('name', 'symbol')
    list_filter = ('market_cap',)
