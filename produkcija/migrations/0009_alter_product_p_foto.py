# Generated by Django 4.1.3 on 2023-02-04 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkcija', '0008_alter_product_p_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='p_foto',
            field=models.ImageField(default='default.jpg', null=True, upload_to=''),
        ),
    ]
