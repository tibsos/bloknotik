from django.shortcuts import render

from .models import *

def home(request):

    user = request.user

    folders = Folder.objects.filter(user = user)
    notes = Note.objects.filter(user = user)

    c = {}

    c['folders'] = folders
    c['notes'] = notes

    return render(request, 'home.html', c)


def create_folder(request):

    Folder.objects.create(user = request.user, title = request.POST.get('title'))

    return render(request, 'components/folder-list.html', {'folders': Folder.objects.filter(user = request.user)})