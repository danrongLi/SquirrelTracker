# Generated by Django 2.2.7 on 2019-12-03 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SquirrelFinder', '0002_auto_20191203_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirreltracker',
            name='Date',
            field=models.CharField(help_text='date', max_length=50),
        ),
    ]
