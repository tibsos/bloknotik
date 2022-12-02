from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import *

def home(request):

    user = request.user

    folders = Folder.objects.filter(user = user)
    notes = Note.objects.filter(user = user)

    # delete_deleted_notes(notes)

    c = {}

    c['folders'] = folders
    c['notes'] = notes

    return render(request, 'home.html', c)


def create_folder(request):

    Folder.objects.create(user = request.user, title = request.POST.get('title'))

    return render(request, 'components/folders.html', {"folders": Folder.objects.filter(user = request.user)})

def delete_folder(request, uid):

    get_object_or_404(Folder, uid = uid).delete()

    return render(request, 'components/folders.html', {"folders": Folder.objects.filter(user = request.user)})

def edit_folder(request, uid):

    folder = get_object_or_404(Folder, uid = uid)

    folder.title = request.POST.get('title')
    folder.color = request.POST.get('color')
    folder.save()

    return HttpResponse('K')


def create_note(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    Note.objects.create(title = title, content = content)

    notes = Note.objects.filter(user = request.user)

    return render(request, 'notes.html', {"notes": notes})

def pin_note(request, uid):

    note = get_object_or_404(Note, uid)

    note.pinned = not note.pinned

    notes = Note.objects.filter(user = request.user)

    return render(request, 'notes.html', {"notes": notes})

def archive_note(request, uid):

    note = get_object_or_404(Note, uid)

    note.archived = not note.archived

    notes = Note.objects.filter(user = request.user)

    return render(request, 'notes.html', {"notes": notes})

def delete_note(request, uid):

    note = get_object_or_404(Note, uid)

    note.deleted = not note.deleted

    notes = Note.objects.filter(user = request.user)

    return render(request, 'notes.html', {"notes": notes})


def edit_note(request, uid):

    note = get_object_or_404(Note, uid)
    
    note.title = request.POST.get('title')
    note.content = request.POST.get('content')

    note.save()

    return HttpResponse('K')