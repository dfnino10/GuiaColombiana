# Generated by Django 2.2.1 on 2019-09-02 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AdministracionGuia', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
