from django.shortcuts import render
from .models import Cart


def cart_home(res):
    cart_obj,new_obj = Cart.objects.new_or_get(res)
    products = cart_obj.products.all()
    total=0
    for x in products:
        total += x.price
    print(total)
    cart_obj.total = total
    cart_obj.save()
    return render(res,"carts/home.html",{})