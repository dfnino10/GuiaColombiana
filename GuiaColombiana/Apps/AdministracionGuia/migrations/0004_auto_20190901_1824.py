# Generated by Django 2.2.4 on 2019-09-01 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionGuia', '0003_auto_20190901_1813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='apellidos',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='nombres',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='usuario',
        ),
    ]
