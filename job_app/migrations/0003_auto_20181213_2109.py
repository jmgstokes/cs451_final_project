# Generated by Django 2.1.4 on 2018-12-13 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0002_auto_20181213_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='fname',
            new_name='title',
        ),
    ]