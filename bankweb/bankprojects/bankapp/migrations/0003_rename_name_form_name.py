# Generated by Django 4.1.7 on 2023-12-05 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_rename_phone_form_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='form',
            old_name='name',
            new_name='Name',
        ),
    ]