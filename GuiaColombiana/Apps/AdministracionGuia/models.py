from django.db import models

# Create your models here.

CATEGORIAS = (('Mu','Museos'), ('Re','Restaurantes'), ('Bic','Paseos de Bicileta'), ('SO', 'Sitios ocultos'))

class Guia(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Documento = models.CharField(max_length=11)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    Sexo=models.CharField(max_length=1, choices=SEXOS, default='M')
    Descripcion= models.CharField(max_length=200)
    Categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='Mu')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Usuario(models.Model):
    ApellidoPaterno = models.CharField(max_length=35)
    ApellidoMaterno = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=35)
    Documento = models.CharField(max_length=11)
    FechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    Sexo=models.CharField(max_length=1, choices=SEXOS, default='M')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.ApellidoPaterno, self.ApellidoMaterno, self.Nombres)

    def __str__(self):
        return self.NombreCompleto()

class Tour(models.Model):
    Nombre = models.CharField(max_length=35)
    Precio = models.CharField(max_length=11)
    Categoria = models.CharField(max_length=30, choices=CATEGORIAS, default='Mu')
