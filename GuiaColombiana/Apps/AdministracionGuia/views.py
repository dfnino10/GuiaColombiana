import json

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView

from .models import UserForm, Guia
=======
from django.core.checks import messages
from django.db import transaction

from django.shortcuts import render
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from .models import UserForm, Guia, Tour, Ciudad, Categoria, Ciudad, UsuarioForm

>>>>>>> b2f7ed0de60f4ca3fedb14b1293e2938ed089558

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
            documento=documento,
            fechaNacimiento=fechaNacimiento,
            password=password,
            sexo=sexo,
            telefono=telefono,
            user = user_model
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


@csrf_exempt
def search_guia_service(request):

    guia = Guia.objects.all()
    guia_json = serializers.serialize("json", guia)
    struct = json.loads(guia_json)
    return JsonResponse(struct, safe=False)


@csrf_exempt
def get_tour(request):
    try:
        pk = request.GET['pk']
        tour = Tour.objects.get(guia_id=pk)
    except Tour.DoesNotExist:
        response = {'mensajeError': 'No existen registro para el Id = ' + pk }
        return JsonResponse(response, safe=False)
    except MultiValueDictKeyError:
        response = {'mensajeError': 'Campo pk es obligatorio'}
        return JsonResponse(response, safe=False)
    
    tour_json = serializers.serialize("json", [tour])
    struct = json.loads(tour_json)
    return JsonResponse(struct, safe=False)

@login_required
def user_profile_view(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        usuario_form = UsuarioForm(request.POST, instance=request.user.usuario)
        context = {
            "user_form": user_form,
            "usuario_form": usuario_form,
        }
        if user_form.is_valid() and usuario_form.is_valid():
            user_form.save()
            usuario_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return render(request, "profile.html", context)
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UsuarioForm(instance=request.user.profile)

    return render(request, "profile.html", context)


@csrf_exempt
def get_ciudad(request):
    ciudades = Ciudad.objects.all()
    ciudades_json = serializers.serialize("json", ciudades)
    struct = json.loads(ciudades_json)
    return JsonResponse(struct, safe=False)

@csrf_exempt
def get_categoria(request):
    categorias = Categoria.objects.all()
    catergorias_json = serializers.serialize("json", categorias)
    struct = json.loads(catergorias_json)
    return JsonResponse(struct, safe=False)

