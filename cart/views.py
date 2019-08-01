from django.shortcuts import render
from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    request.session["cart_id"] = "12"
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print("Cart ID exist")
        cart_obj = qs.first()
    else:
        cart_obj = Cart.objects.new_cart(user=request.user)
        request.session["cart_id"] = cart_obj.id
    return render(request, "cart/home.html", {})