# Generated by Django 3.2.10 on 2021-12-19 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repertoire', '0002_rename_filename_work_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='contrubutors',
            new_name='contributors',
        ),
    ]
