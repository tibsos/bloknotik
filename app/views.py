from django.shortcuts import render, HttpResponse, get_object_or_404

from django.contrib.auth.decorators import login_required as lr

from .models import *

@lr
def home(request):

    user = request.user

    folders = Folder.objects.filter(user = user)
    notes = Note.objects.filter(user = user).filter(deleted = False)

    # delete_deleted_notes(notes)

    c = {}

    c['folders'] = folders
    c['notes'] = notes

    return render(request, 'home.html', c)

@lr
def create_folder(request):

    Folder.objects.create(user = request.user, title = request.POST.get('title'))

    return render(request, 'components/folders.html', {"folders": Folder.objects.filter(user = request.user)})

@lr
def delete_folder(request, uid):

    get_object_or_404(Folder, uid = uid).delete()

    return render(request, 'components/folders.html', {"folders": Folder.objects.filter(user = request.user)})

@lr
def edit_folder(request, uid):

    folder = get_object_or_404(Folder, uid = uid)

    folder.title = request.POST.get('title')
    folder.color = request.POST.get('color')
    folder.save()

    return HttpResponse('K')

@lr
def create_note(request):

    title = request.POST.get('title')
    content = request.POST.get('content')

    Note.objects.create(user = request.user, title = title, content = content)

    notes = Note.objects.filter(user = request.user).filter(deleted = False)

    return render(request, 'components/notes.html', {"notes": notes})

@lr
def get_note(request, uid):

    return render(request, 'components/note.html', {"note": get_object_or_404(Note, uid = uid)})

@lr
def love_note(request):

    return HttpResponse('K')

@lr
def pin_note(request, uid):

    note = get_object_or_404(Note, uid = uid)

    note.pinned = not note.pinned

    notes = Note.objects.filter(user = request.user)

    return render(request, 'components/notes.html', {"notes": notes})

@lr
def archive_note(request, uid):

    note = get_object_or_404(Note, uid = uid)

    note.archived = not note.archived

    notes = Note.objects.filter(user = request.user)

    return render(request, 'components/notes.html', {"notes": notes})

@lr
def delete_note(request, uid):

    note = get_object_or_404(Note, uid = uid)
    note.deleted = not note.deleted
    note.save()

    notes = Note.objects.filter(user = request.user).filter(deleted = False)

    return render(request, 'components/notes.html', {"notes": notes})

@lr
def add_image(request, uid):

    note = get_object_or_404(Note, uid = uid)

    image = Image.objects.create(user = request.user, file = request.FILES.get('file'))

    note.images.add(image)

    # handle error

    return render(request, 'components/note-images.html', {'note': note})

@lr
def edit_note(request, uid):

    note = get_object_or_404(Note, uid)
    
    note.title = request.POST.get('title')
    note.content = request.POST.get('content')

    note.save()

    return HttpResponse('K')

@lr
def change_note_color(request):

    note = get_object_or_404(Note, uid = request.POST.get('uid'))

    note.color = request.POST.get('color')
    note.background = None
    note.save()

    return HttpResponse('K')