# Generated by Django 3.1.3 on 2020-11-07 20:19

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=40, unique=True, verbose_name='Nombre de usuario')),
                ('en_linea', models.BooleanField(default=False)),
                ('fecha_ultima_sesion', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'swappable': 'AUTH_USER_MODEL',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
