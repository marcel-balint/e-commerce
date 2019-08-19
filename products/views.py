from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Product
#
from django.views.generic import DetailView
from cart.models import Cart


def product_list(request):
    queryset = Product.objects.all()
    context = {
        "qs": queryset
    }
    return render(request, "products/product_list.html", context)


def product_detail(request, pk):
    instance = get_object_or_404(Product, pk=pk)
    qs = Product.objects.filter(id=pk)
    if qs.exists() and qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Product doesn't exist")
    context = {
        "object": instance
    }
    return render(request, "products/product_detail.html", context)


class ProductDetailSlugView(DetailView):
    template = "products/product_detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(
            ProductDetailSlugView,
            self).get_context_data(
            *
            args,
            **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context
