# Generated by Django 4.1.3 on 2022-11-06 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0003_rename_s_apraksts_saimnieciba_apraksts_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='apraksts',
            new_name='s_apraksts',
        ),
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='foto',
            new_name='s_foto',
        ),
        migrations.RenameField(
            model_name='saimnieciba',
            old_name='nosaukums',
            new_name='s_nosaukums',
        ),
    ]