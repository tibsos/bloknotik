from django.urls import path

from .views import donate

urlpatterns = [

    path('donate/', donate, name = 'donate'),    

]