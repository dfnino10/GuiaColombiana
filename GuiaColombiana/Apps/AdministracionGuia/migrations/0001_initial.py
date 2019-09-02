# Generated by Django 2.2.4 on 2019-09-02 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.CharField(max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Guia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidoPaterno', models.CharField(max_length=35)),
                ('apellidoMaterno', models.CharField(max_length=35)),
                ('nombres', models.CharField(max_length=35)),
                ('documento', models.CharField(max_length=11)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
                ('descripcion', models.CharField(max_length=200)),
                ('categoria', models.ForeignKey(null=True, on_delete='', to=settings.AUTH_USER_MODEL)),
                ('ciudad', models.ForeignKey(null=True, on_delete='', to='AdministracionGuia.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documento', models.CharField(max_length=11, null=True)),
                ('fechaNacimiento', models.DateField(null=True)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1, null=True)),
                ('telefono', models.CharField(max_length=10, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=35)),
                ('precio', models.CharField(max_length=11)),
                ('descripcion', models.CharField(max_length=1000)),
                ('guia', models.ForeignKey(null=True, on_delete='', to='AdministracionGuia.Guia')),
            ],
        ),
    ]
