# Generated by Django 2.2.7 on 2019-12-07 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SquirrelFinder', '0007_auto_20191206_1936'),
    ]

    operations = [
        migrations.RenameField(
            model_name='squirreltracker',
            old_name='Color_Note',
            new_name='Color_Notes',
        ),
    ]
