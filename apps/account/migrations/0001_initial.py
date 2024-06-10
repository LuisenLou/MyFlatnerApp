# Generated by Django 5.0.6 on 2024-06-10 11:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('birth_date', models.DateField()),
                ('genre', models.CharField(choices=[('M', 'Masculino'), ('W', 'Femenino'), ('N', 'Prefiero no decirlo')], max_length=1)),
                ('country', models.CharField(max_length=20)),
                ('province_or_state', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('ocupation', models.CharField(choices=[('Estudiante', 'Student'), ('Trabajador', 'Worker')], max_length=15)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('description', models.TextField(blank=True, max_length=255, null=True)),
                ('role', models.CharField(choices=[('Inquilino', 'Tenant'), ('Propietario', 'Landlord')], max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
