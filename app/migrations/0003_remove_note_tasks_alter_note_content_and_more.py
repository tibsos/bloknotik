# Generated by Django 4.1.3 on 2022-11-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_folder_color_note_content_note_premium_note_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='tasks',
        ),
        migrations.AlterField(
            model_name='note',
            name='content',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
