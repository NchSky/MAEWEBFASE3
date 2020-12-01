from django.contrib import admin

# Register your models here.
from . models import Entrada,Formulario

admin.site.register(Entrada)
admin.site.register(Formulario)