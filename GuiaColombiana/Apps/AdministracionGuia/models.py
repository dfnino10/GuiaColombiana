from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
# Create your models here.

CATEGORIAS = (('Mu','Museos'), ('Re','Restaurantes'), ('Bic','Paseos de Bicileta'), ('SO', 'Sitios ocultos'))

class Guia(models.Model):
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    documento = models.CharField(max_length=11)
    fechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    sexo=models.CharField(max_length=1, choices=SEXOS, default='M')
    descripcion= models.CharField(max_length=200)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='Mu')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        return self.NombreCompleto()

class Usuario(models.Model):
    apellidos = models.CharField(max_length=100)
    nombres = models.CharField(max_length=100)
    documento = models.CharField(max_length=11)
    fechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M')
    usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)

    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.apellidos, self.nombres)

    def __str__(self):
        return self.NombreCompleto()

class Tour(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.CharField(max_length=11)
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='Mu')


class UserForm (ModelForm):
    class Meta:
        model = Usuario
        fields = ['apellidos', 'nombres', 'documento', 'fechaNacimiento', 'sexo', 'usuario', 'password', 'telefono', 'correo']
