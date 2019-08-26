import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from .models import UserForm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import UserForm

from .models import Usuario


# Create your views here.


def register_user_view(request):
    form = UserForm()
    return render(request, 'register.html', {'form': form})


@csrf_exempt
def add_user_view(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        apellidos = jsonUser['apellidos']
        nombres = jsonUser['nombres']
        documento = jsonUser['documento']
        fechaNacimiento = jsonUser['fechaNacimiento']
        password = jsonUser['password']
        sexo = jsonUser['sexo']
        usuario = jsonUser['usuario']
        telefono = jsonUser['telefono']
        correo = jsonUser['correo']

        user_model = User.objects.create_user(username=usuario, password=password)
        user_model.first_name = nombres
        user_model.last_name = apellidos
        user_model.email = correo
        user_model.save()

        newUser = Usuario(
            apellidos=apellidos,
            nombres=nombres,
            documento=documento,
            fechaNacimiento =fechaNacimiento,
            password=password,
            sexo=sexo,
            usuario=usuario,
            telefono=telefono,
            correo=correo,
        )
        newUser.save()
    return HttpResponse(serializers.serialize("json", [user_model]))
