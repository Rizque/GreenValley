# Generated by Django 4.1.3 on 2022-12-03 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produkcija', '0003_remove_produkts_saimnieciba_produkts_p_datums'),
        ('saimniecibas', '0007_profile_delete_saimnieciba'),
    ]

    operations = [
        migrations.AddField(
            model_name='produkts',
            name='saimieciba',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='saimniecibas.profile'),
        ),
    ]