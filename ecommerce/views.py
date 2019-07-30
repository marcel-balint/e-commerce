from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    context = {
        "title": "Home page",
        "content": "This will be the content"
    }
    return render(request, "home_page.html", context)
    
    
def about_page(request):
    context = {
        "title": "About page",
        "content": "This will be the content of about"
    }
    return render(request, "about_page.html", context)    
    
    
def contact_page(request):
    context = {
        "title": "Contact page",
        "content": "This will be the content of contact"
    }
    return render(request, "contact_page.html", context)    