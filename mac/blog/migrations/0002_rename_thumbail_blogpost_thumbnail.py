# Generated by Django 4.0.1 on 2022-02-28 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='thumbail',
            new_name='thumbnail',
        ),
    ]
