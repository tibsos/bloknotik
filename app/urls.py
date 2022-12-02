from django.urls import path

from .views import *

app_name = 'app'

urlpatterns = [

    path('home/', home, name = 'home'),

]

htmx_urlpatterns = [

    path('create-folder/', create_folder, name = 'create-folder'),
    path('edit-folder/<uuid:uid>/', edit_folder, name = 'edit-folder'),
    path('delete-folder/<uuid:uid>/', delete_folder, name = 'delete-folder'),

    path('create-note/', create_note, name = 'create-note'),
    path('get-note/<uuid:uid>/', get_note, name = 'get-note'),
    path('pin-note/<uuid:uid>/', pin_note, name = 'pin-note'),
    path('acrhive-note/<uuid:uid>/', archive_note, name = 'acrhive-note'),
    path('delete-note/<uuid:uid>/', delete_note, name = 'delete-note'),
    path('add-image/<uuid:uid>/', add_image, name = 'add-image')

]

ajax_urlpatterns = [

    path('edit-note/<uuid:uid>/', edit_note, name = 'edit-note'),
    path('love-note/', love_note, name = 'love-note'),
    path('change-note-color', change_note_color, name = 'change-note-color'),

]

urlpatterns += htmx_urlpatterns
urlpatterns += ajax_urlpatterns