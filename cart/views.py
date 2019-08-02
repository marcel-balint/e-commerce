from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from products.models import Product


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    return render(request, "cart/home.html", {"cart": cart_obj})
    

def cart_update(request):
    product_id = int(request.POST['product_id'])
    print(int(request.POST['product_id']))
    print(product_id)
    
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
            
            print(product_id)
            
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj) 
        request.session['cart_items'] = cart_obj.products.count()
        
    return redirect("cart:home")    

