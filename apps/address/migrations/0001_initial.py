# Generated by Django 5.0.6 on 2024-06-10 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('via_class', models.CharField(choices=[('CALLE', 'Calle'), ('AVENIDA', 'Avenida'), ('PLAZA', 'Plaza'), ('CAMINO', 'Camino'), ('PASEO', 'Paseo'), ('CARRETERA', 'Carretera'), ('AUTOPISTA', 'Autopista'), ('RAMBLA', 'Rambla'), ('TRAVESÍA', 'Travesía'), ('GLORIETA', 'Glorieta'), ('RONDA', 'Ronda'), ('CARRERA', 'Carrera'), ('VÍA', 'Vía'), ('PASAJE', 'Pasaje'), ('BULEVAR', 'Bulevar')], max_length=20)),
                ('via_name', models.CharField(max_length=50)),
                ('via_number', models.IntegerField()),
                ('floor', models.CharField(blank=True, max_length=3)),
                ('door', models.CharField(blank=True, max_length=3)),
                ('postal_code', models.CharField(max_length=6)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
            ],
        ),
    ]