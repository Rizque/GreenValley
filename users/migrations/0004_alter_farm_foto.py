# Generated by Django 4.1.3 on 2023-06-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_first_name_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]