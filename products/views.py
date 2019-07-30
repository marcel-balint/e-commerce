from django.shortcuts import render
from .models import Product


def product_list(request):
    queryset = Product.objects.all()
    context = {
        "qs": queryset
    }
    return render(request, "products/product_list.html", context)