# Generated by Django 4.1.3 on 2022-12-03 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0009_profile_username'),
        ('produkcija', '0005_alter_produkts_saimieciba'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produkts',
            new_name='Product',
        ),
    ]
