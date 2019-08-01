from django.shortcuts import render


def cart_home(request):
    print(request.session)
    return render(request, "cart/home.html")