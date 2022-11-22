from django.urls import path

from django.conf import settings

from django.contrib.auth.views import LogoutView
from .views import *

app_name = 'user'

urlpatterns = [

    path('login/', log_in, name = 'login'),
    path('register/', register, name = 'register'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name = 'logout'),

]