"""GuiaColombiana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from GuiaColombiana.Apps.AdministracionGuia import views

urlpatterns = [
    url(r'^register/$', views.register_user_view, name='register'),
    url(r'^addUser/$', views.add_user_view, name='addUser'),
    url(r'^login/$', views.login_method, name='login'),
    url(r'^index/$', views.login_view, name='index'),
    url(r'^search/$', views.search_guia_service, name='search'),
    url(r'^getTour/$', views.get_tour, name='getTour'),
    url(r'^getCiudad/$', views.get_ciudad, name='getCiudad'),
    url(r'^getCategorias/$', views.get_categoria, name='getCategorias'),
    url(r'^getGuides/$', views.view_all_guides, name='getGuides'),
    path('profile/', views.user_profile_view, name='profile'),
    url(r'^sendEmail/$', views.send_email_view, name='email'),
]
