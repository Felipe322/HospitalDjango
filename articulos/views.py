from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from .models import Articulo
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, AccessMixin


class Lista(LoginRequiredMixin, ListView):
    model = Articulo
    paginate_by = 5

def comprar(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    if articulo.stock > 0:
        articulo.stock = articulo.stock - 1
        articulo.save()

        id = str(pk)

        request.session['total'] = request.session['total'] + float(articulo.precio)
        request.session['cuantos'] = request.session['cuantos'] + 1

        if id in request.session['articulos']:
            request.session['articulos'][id]['cantidad'] = request.session['articulos'][id]['cantidad'] + 1
        else:
            request.session['articulos'][id] = {'precio':float(articulo.precio), 'cantidad': 1}

        
    
    print(request.session['articulos'])

    return redirect('articulos:lista')

