from django.urls import path

from .views import *

urlpatterns = [

    path('landing/', landing, name = 'landing'),

]