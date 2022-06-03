from django.contrib import admin
from .models import Paciente, Estado, Municipio


admin.site.register(Paciente)
admin.site.register(Estado)
admin.site.register(Municipio)