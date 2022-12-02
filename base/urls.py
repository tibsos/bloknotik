from django.urls import path

from .views import *

app_name = 'base'

urlpatterns = [

    path('', landing, name = 'landing'),

    path('plans/', plans, name = 'plans'),

    path('contact-us/', contact, name = 'contact'),

    # Info
    path('terms/', terms, name = 'terms'),
    path('privacy/', privacy, name = 'privacy'),
    path('juridical-information/', juridical, name = 'juridical'),
    path('online-payment-safety/', online_payment_safety, name = 'online-payment-safety'),
    path('data-safety/', data_safety, name = 'data-safety'),

]