from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm


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
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact page",
        "content": "This will be the content of contact",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact_page.html", context)    
    
    
def login_page(request):
    form = LoginForm()
    context = {
        "form": form
    }
    print("User logged in")
    print(request.user.is_authenticated())
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated())
        if user is not None:
            login(request, user)
            print("User logged in")
            print(request.user.is_authenticated())
            context["form"] = LoginForm()
            return redirect("/login")
        else:
            print("error")
    return render(request, "auth/login.html", context)
    
    
def register_page(request):
    return render(request, "auth/register.html", {})    