import os

from django.db import models as m

from django.contrib.auth.models import User

from uuid import uuid4 as u4

def upload_image(instance, filename):

    file_extension = filename.split('.')[-1]

    new_filename = f"{u4}.{file_extension}"

    return os.path.join('uploads/note/image', new_filename)

def upload_note_background(instance, filename):

    file_extension = filename.split('.')[-1]

    new_filename = f"{u4}.{file_extension}"

    return os.path.join('uploads/note/background', new_filename)

class Folder(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    uid = m.UUIDField(default = u4)

    title = m.CharField(max_length = 500)

    color = m.CharField(max_length = 7)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['updated_at']

class Task(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    uid = m.UUIDField(default = u4)

    title = m.CharField(max_length = 500, blank = True)

    completed = m.BooleanField(default = False)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        if self.title:

            return f"{self.title} by {self.user.username}"

class Image(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    uid = m.UUIDField(default = u4)

    file = m.ImageField(upload_to = upload_image)

    uploaded_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return f"{self.user.username} image"

    class Meta:

        ordering = ['uploaded_at']

class Background(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    uid = m.UUIDField(default = u4)

    file = m.ImageField(upload_to = upload_note_background)

    uploaded_at = m.DateTimeField(auto_now_add = True)

    def __str__(self):

        return f"{self.user.username} | note background"

    class Meta:

        ordering = ['uploaded_at']

class Note(m.Model):

    user = m.ForeignKey(User, on_delete = m.CASCADE)

    uid = m.UUIDField(default = u4)

    title = m.CharField(max_length = 1000)
    content = m.TextField()

    background_color = m.CharField(max_length = 7)
    background_image = m.ForeignKey(Background, on_delete = m.DO_NOTHING, null = True)

    folders = m.ManyToManyField(Folder, blank = True)
    images = m.ManyToManyField(Image, blank = True)
    tasks = m.ManyToManyField(Task, blank = True)

    archived = m.BooleanField(default = False)
    deleted = m.BooleanField(default = False)

    premium = m.BooleanField(default = False)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return f"{self.title} by {self.user.username}"

    class Meta:

        ordering = ['updated_at']