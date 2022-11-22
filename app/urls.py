from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home'),

]

ajax_urlpatterns = [

    path('create-folder/', create_folder, name = 'create-folder'),

]

urlpatterns += ajax_urlpatterns