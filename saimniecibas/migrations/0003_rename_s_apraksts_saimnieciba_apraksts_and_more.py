# Generated by Django 4.1.3 on 2022-11-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0002_rename_apraksts_saimnieciba_s_apraksts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='s_apraksts',
            new_name='apraksts',
        ),
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='s_foto',
            new_name='foto',
        ),
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='s_nosaukums',
            new_name='nosaukums',
        ),
    ]
