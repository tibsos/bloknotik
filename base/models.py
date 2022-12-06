from django.db import models as m

from django.contrib.auth.models import User

from tinymce.models import HTMLField

class Info(m.Model):

    title = m.CharField(max_length = 300)

    content = HTMLField() 

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['-title']


class FutureFeature(m.Model):

    title = m.TextField()
    description = m.TextField()

    internal = m.BooleanField(default = False)

    completed = m.BooleanField(default = False)
    completion_date = m.DateField(blank = True)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        return self.title

    class Meta:

        ordering = ['title']

class UserFeedback(m.Model):

    user = m.OneToOneField(User, on_delete = m.CASCADE, null = True, related_name = 'user_feedback')
    anonymous = m.BooleanField(default = True)

    name = m.TextField(blank = True)

    feedback = m.TextField(blank = True)
    rating = m.PositiveSmallIntegerField(default = 5)

    created_at = m.DateTimeField(auto_now_add = True)
    updated_at = m.DateTimeField(auto_now = True)

    def __str__(self):

        if self.user:

            return self.user.username

    class Meta:

        ordering = ['-updated_at']