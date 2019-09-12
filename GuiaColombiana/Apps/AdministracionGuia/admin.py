from django.contrib import admin

from GuiaColombiana.Apps.AdministracionGuia.models import *

# Register your models here.
admin.site.register(Guia)
admin.site.register(Usuario)
admin.site.register(Tour)
admin.site.register(Ciudad)
admin.site.register(Categoria)