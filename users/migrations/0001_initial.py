# Generated by Django 4.1.3 on 2023-06-03 18:53

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=200)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=500)),
                ('foto', models.ImageField(default='default_profile.jpg', null=True, upload_to='')),
                ('phone', models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{8}$')])),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('foto', models.ImageField(default='default_farm.jpg', null=True, upload_to='')),
                ('phone', models.CharField(blank=True, max_length=8, null=True, validators=[django.core.validators.RegexValidator(regex='^\\d{8}$')])),
                ('country', models.CharField(default='Latvija', max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('latitude', models.CharField(blank=True, max_length=200, null=True)),
                ('longitude', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('foto', models.ImageField(default='default_profile.jpg', null=True, upload_to='')),
                ('person', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
