#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.utils.http import is_safe_url
from .models import BillingProfile, Card
import stripe

STRIPE_SECRET_KEY = settings.STRIPE_SECRET_KEY
STRIPE_PUB_KEY = settings.STRIPE_PUB_KEY

stripe.api_key = STRIPE_SECRET_KEY


def payment_method_view(request):
    (billing_profile, billing_profile_created) = \
        BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect('/cart')
    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
        next_url = next_
    return render(request, 'billing/payment-method.html',
                  {'publish_key': STRIPE_PUB_KEY, 'next_url': next_url})


def payment_method_createview(request):
    if request.method == 'POST' and request.is_ajax():
        (billing_profile, billing_profile_created) = \
            BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({'message': 'Cannot find this user'},
                                status=401)
        token = request.POST.get('token')
        if token is not None:

            # Create a new customer card source based on token

            new_card_obj = Card.objects.add_new(billing_profile, token)
        return JsonResponse({'message': 'Success! Your card was added.'})
    return HttpResponse('error', status=401)
