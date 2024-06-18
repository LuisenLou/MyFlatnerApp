# Generated by Django 5.0.6 on 2024-06-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_form', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_form',
            old_name='street',
            new_name='address_name',
        ),
        migrations.RemoveField(
            model_name='contact_form',
            name='title',
        ),
        migrations.AddField(
            model_name='contact_form',
            name='via',
            field=models.CharField(blank=True, choices=[('Calle', 'Calle'), ('Avenida', 'Avenida'), ('Plaza', 'Plaza'), ('Carretera', 'Carretera'), ('Paseo', 'Paseo'), ('Ronda', 'Ronda')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact_form',
            name='postal_code',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]