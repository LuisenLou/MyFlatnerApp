# Generated by Django 5.0.6 on 2024-06-11 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_account_city_alter_account_country_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.RemoveField(
            model_name='account',
            name='user',
        ),
        migrations.AddField(
            model_name='account',
            name='email',
            field=models.EmailField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='account',
            name='first_name',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_editor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='account',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='account',
            name='last_name',
            field=models.CharField(default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='account',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='account',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]