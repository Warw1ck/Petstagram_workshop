# Generated by Django 4.1.3 on 2023-05-27 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='tagget_pets',
            new_name='tagged_pets',
        ),
    ]
