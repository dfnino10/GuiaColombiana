from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

CATEGORIAS = (('Mu', 'Museos'), ('Re', 'Restaurantes'), ('Bic', 'Paseos de Bicileta'), ('SO', 'Sitios ocultos'))



class Categoria(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=50)

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)

class Guia(models.Model):
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    documento = models.CharField(max_length=11)
    fechaNacimiento = models.DateField()
    SEXOS = (('F', 'Femenino'),('M', 'Masculino'))
    sexo=models.CharField(max_length=1, choices=SEXOS, default='M')
    descripcion= models.CharField(max_length=200)
    categoria =  models.ForeignKey(User, null=True, on_delete='')
    ciudad = models.ForeignKey(Ciudad, null=True, on_delete='')

    def NombreCompleto(self):
        cadena = "{0} {1}, {2}"
        return cadena.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        return self.NombreCompleto()


class Usuario(models.Model):
    documento = models.CharField(max_length=11, null = True)
    fechaNacimiento = models.DateField(null = True )
    SEXOS = (('F', 'Femenino'), ('M', 'Masculino'))
    sexo = models.CharField(max_length=1, choices=SEXOS, default='M',  null = True)
    telefono = models.CharField(max_length=20,  null = True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,  null = True)

    def NombreCompleto(self):
        cadena = "{0}, {1}"
        return cadena.format(self.apellidos, self.nombres)

    def __str__(self):
        return self.NombreCompleto()

    @receiver(post_save, sender=User)
    def create_user_usuario(sender, instance, created, **kwargs):
        if created:
            Usuario.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_usuario(sender, instance, **kwargs):
        instance.usuario.save()


class Tour(models.Model):
    nombre = models.CharField(max_length=35)
    precio = models.CharField(max_length=11)
    descripcion = models.CharField(max_length=1000)
    guia = models.ForeignKey(Guia, null=True, on_delete='')

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['documento', 'fechaNacimiento', 'sexo', 'telefono']
