# Generated by Django 4.2.13 on 2024-06-06 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app44', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logintable',
            old_name='type',
            new_name='usertype',
        ),
    ]
