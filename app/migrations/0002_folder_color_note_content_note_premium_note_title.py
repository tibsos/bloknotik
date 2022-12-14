# Generated by Django 4.1.3 on 2022-11-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='color',
            field=models.CharField(default='black', max_length=7),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default='ss'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='note',
            name='title',
            field=models.CharField(default='w', max_length=1000),
            preserve_default=False,
        ),
    ]
