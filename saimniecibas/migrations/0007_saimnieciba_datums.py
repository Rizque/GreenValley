# Generated by Django 4.1.3 on 2022-11-20 18:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('saimniecibas', '0006_alter_saimnieciba_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='saimnieciba',
            name='datums',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
