# Generated by Django 3.2.5 on 2021-09-02 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mohankala', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='Phone',
            new_name='phone',
        ),
    ]
