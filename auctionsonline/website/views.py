from django.shortcuts import render

def index(request):
   return render(request, 'index.html', {'auctions': auctions})

def bid_page(request, auction_id):
   return index(request)

def comment(request, auction_id):
   return index(request)

def raise_bid(request, auction_id):
   return bid_page(request, auction_id)

def register_page(request):
   return render(request, 'register.html')

def watchlist(request, auction_id):
   return index(request)

def watchlist_page(request):
   return index(request)

def balance(request):
   return index(request)

def topup(request):
   return index(request)

def filter_auctions(request, category):
   return index(request)

def register(request):
   return index(request)

def login_page(request):
   return index(request)

def logout_page(request):
   return index(request)