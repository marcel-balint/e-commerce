from django.shortcuts import render, get_object_or_404
from .models import Product


def product_list(request):
    queryset = Product.objects.all()
    context = {
        "qs": queryset
    }
    return render(request, "products/product_list.html", context)
    
    
def product_detail(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    context = {
        "qs": instance
    }
    return render(request, "products/product_detail.html", context)    
    