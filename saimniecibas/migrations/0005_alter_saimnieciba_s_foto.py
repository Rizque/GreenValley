# Generated by Django 4.1.3 on 2022-11-06 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0004_rename_apraksts_saimnieciba_s_apraksts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saimnieciba',
            name='s_foto',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]