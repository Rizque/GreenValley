# Generated by Django 4.1.3 on 2022-11-06 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('saimniecibas', '0002_rename_apraksts_saimnieciba_s_apraksts_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produkts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nosaukums', models.CharField(max_length=200)),
                ('p_apraksts', models.TextField()),
                ('p_foto', models.ImageField(upload_to='')),
                ('cena', models.DecimalField(decimal_places=2, max_digits=7)),
                ('cenas_mervieniba', models.CharField(choices=[('kg', 'Kilogrami'), ('ml', 'mililitri'), ('l', 'litri'), ('gab', 'gabalā')], max_length=100)),
                ('saimnieciba', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='saimniecibas.saimnieciba')),
            ],
        ),
    ]
