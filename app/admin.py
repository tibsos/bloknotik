from django.contrib import admin as a

from .models import *

a.site.register(Background)
a.site.register(Image)
a.site.register(Task)
a.site.register(Note)
a.site.register(Folder)