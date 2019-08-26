import json

from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse
from .models import UserForm, Guia

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from .models import Usuario


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


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


def login_view(request):
    return render(request, 'index.html')


@csrf_exempt
def login_method(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'Bienvenido ' + username
        else:
            message = 'Usuario o contrasenia incorrectos.'

        return JsonResponse({'message': message})


def view_all_guides(request):
    guides_list = Guia.objects.all()
    context = {'guides_list': guides_list}
    return render(request, 'guides.html', context)