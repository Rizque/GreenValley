# Generated by Django 4.1.3 on 2022-12-11 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0010_alter_profile_s_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='s_foto',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
