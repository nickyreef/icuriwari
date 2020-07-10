from django.contrib import admin

# Register your models here.
from .models import User, Product, Auction, Chat, Watchlist, Bid

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Chat)
admin.site.register(Watchlist)
admin.site.register(Bid)