# Generated by Django 5.0.6 on 2024-06-10 12:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='elevator',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='flat',
            name='renovated',
            field=models.BooleanField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='viewcount',
            name='flat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flat_view_count', to='flat.flat'),
        ),
    ]