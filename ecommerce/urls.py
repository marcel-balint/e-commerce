"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include  
from django.contrib import admin
from accounts.views import login_page, register_page
from .views import home_page, about_page, contact_page
from products.views import product_list, product_detail
from django.views.static import serve
from cart.views import cart_home
from .settings import MEDIA_ROOT


urlpatterns = [
    url(r'^$', home_page, name="home"),
    url(r'^about/$', about_page, name="about"),
    url(r'^contact/$', contact_page, name="contact"),
    url(r'^login/$', login_page, name="login"),
    #url(r'^cart/$', cart_home, name="cart"),
    url(r'^cart/', include("cart.urls", namespace="cart")),
    url(r'^register/$', register_page, name="register"),
    url(r'^products/$', product_list, name="products"),
    url(r'^products/(?P<pk>\d+)/$', product_detail, name="product_detail"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^admin/', admin.site.urls),
]
