from django.contrib.auth import authenticate, login
from django.core.serializers import json
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserForm
from django.contrib.auth.models import User
from django.shortcuts import render
import json
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario


# Create your views here.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_method(request):
    if request.method == 'POST':
        jsonUser = json.loads(request.body)
        username = jsonUser['username']
        password = jsonUser['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            message = 'Ok'
        else:
            message = 'Not ok'

        return JsonResponse({'message': message})


def register_user_view(request):
    form = UserForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    return render(request, 'index.html')


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
        user_model.nombres = nombres
        user_model.apellidos = apellidos
        user_model.documento = documento
        user_model.fechaNacimiento = fechaNacimiento
        user_model.sexo = sexo
        user_model.telefono = telefono
        user_model.correo = correo
        user_model.save()

    return HttpResponse(serializers.serialize("json", [user_model]))

