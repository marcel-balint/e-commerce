from django.conf.urls import url
from .views import product_list

urlpatterns = [
    url('^$', product_list, name="product_list")
]