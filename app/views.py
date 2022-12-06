from django.shortcuts import render, HttpResponse, get_object_or_404

from django.contrib.auth.decorators import login_required as lr

from .models import *

import datetime

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
def get_folder(request, uid):

    folder = get_object_or_404(Folder, uid = uid)

    return render(request, 'components/notes.html', {'notes': Note.objects.filter(user = request.user).filter(folders__in = [folder]).filter(deleted = False).filter(archived = False).order_by('updated_at')})

@lr 
def archive(request):
    return render(request, 'components/notes.html', {'notes': Note.objects.filter(user = request.user).filter(deleted = False).filter(archived = True).order_by('updated_at')})

@lr 
def trash(request):
    return render(request, 'components/notes.html', {'notes': Note.objects.filter(user = request.user).filter(deleted = False).order_by('updated_at')})

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

    Note.objects.create(user = request.user,
        title = request.POST.get('title'), 
        content = request.POST.get('content'),
        color = request.POST.get('color'))

    notes = Note.objects.filter(user = request.user).filter(deleted = False)

    return render(request, 'components/notes.html', {"notes": notes})

@lr
def add_image_to_new_note(request):

    image = Image.objects.create(user = request.user, file = request.FILES.get('file'))

    return render(request, 'components/new-note-images.html', )



@lr
def get_note(request, uid):

    note = get_object_or_404(Note, uid = uid)

    # Edit date

    c = {}

    month_list = [

        'Января',
        'Февраля',
        'Марта',
        'Апреля',
        'Мая',
        'Июня',
        'Июля',
        'Февраля',
        'Сентября',
        'Октября',
        'Ноября',
        'Декабря',

    ]

    edit_datetime = note.updated_at
    minute, hour, day, month, year = edit_datetime.minute, edit_datetime.hour, edit_datetime.day, edit_datetime.month, edit_datetime.year

    now = datetime.datetime.now()

    if year == now.year:

        if month == now.month:

            if day == now.day:

                if hour == now.hour:
                    
                    minutes_ago = now.minute - minute

                    c['edited_at'] = f"{minutes_ago} минут назад"

                else:

                    hours_ago = now.hour - hour

                    if hours_ago == 1:

                        c['edited_at'] = f"1 час назад"

                    elif hours_ago < 5:

                        c['edited_at'] = f"{hours_ago} часа назад"

                    else:

                        c['edited_at'] = f"{hours_ago} часов назад"

            else:

                if hour < 10:

                    hour = f"0{hour}"
                
                if minute < 10:

                    minute = f"0{minute}"


                if now.day - day == 1:

                    c['edited_at'] = f'Вчера в {hour}:{minute}'

                elif now.day - day == 2:

                    c['edited_at'] = f'Позавчера в {hour}:{minute}'

                else:

                    c['edited_at'] = f"{day} {month_list[month]}"
        else:

            c['edited_at'] = f"{day} {month_list[month]}"
    
    else:

        c['edited_at'] = f"{day} {month_list[month]}, {year}"

    print(c['edited_at'])


    return render(request, 'components/note.html', c)

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

    image = Image.objects.create(user = request.user, file = request.FILES.get('image'))

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