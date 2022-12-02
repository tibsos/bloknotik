from django.db import models as m

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