from django.urls import path
from .views import Login, Nuevo, Perfil, ActivarCuenta, Principal
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('', Principal.as_view(), name='login'),

    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('nuevo/', Nuevo.as_view(), name='nuevo'),
    path('perfil/', Perfil.as_view(), name='perfil'),
    path('activar/<slug:uidb64>/<slug:token>', ActivarCuenta.as_view(), name='activar')


]
