from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Paciente, Municipio, Estado
from .forms import PacienteForm
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin


class Lista(PermissionRequiredMixin, ListView):
    permission_required = 'usuarios.permiso_administradores'
    paginate_by = 5
    model = Paciente


class Nuevo(LoginRequiredMixin, CreateView):
    model = Paciente
    form_class = PacienteForm
    
    success_url = reverse_lazy('pacientes:lista')

class Editar(UpdateView):
    model = Paciente
    form_class = PacienteForm
    extra_context = {'editar':True}

    success_url = reverse_lazy('pacientes:lista')

class Eliminar(DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes:lista')


def buscar_municipio(request):
    id_estado = request.POST.get('id',None)
    if id_estado:
        municipios = Municipio.objects.filter(estado_id=id_estado)
        data = [{'id':mun.id,'nombre':mun.nombre} for mun in  municipios]
        return JsonResponse(data, safe=False)
    return JsonResponse({'error':'Parámetro inválido'}, safe=False)
