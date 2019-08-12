from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Home page",
        "content": "This will be the content",
    }
    if request.user.is_authenticated():
        context["login"] = "Logged in content"
    return render(request, "home_page.html", context)
    
    
def about_page(request):
    context = {
        "title": "About page",
        "content": "This will be the content of about"
    }
    return render(request, "about_page.html", context)    
    
    
def contact_page(request):
    form = ContactForm(request.POST)
    if request.method == 'POST': 
        form = ContactForm(request.POST)
        if form.is_valid():
            form = ContactForm()
    context = {
        "title": "Contact page",
        "content": "This will be the content of contact",
        "form": form,
    }
    return render(request, "contact_page.html", context)    
    
