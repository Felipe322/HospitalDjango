from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from .forms import UsuarioForm, PerfilForm
from .models import Usuario
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from .token import token_activacion
from django.contrib.auth.mixins import LoginRequiredMixin


class Principal(LoginRequiredMixin, TemplateView):
    template_name = "bienvenida.html"

class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get_success_url(self):
        self.request.session['cuantos'] = 0
        self.request.session['total'] = 0.0
        self.request.session['articulos'] = {}


        return super().get_success_url()

class Nuevo(CreateView):
    template_name = 'nuevo.html'
    model = Usuario
    form_class = UsuarioForm
    success_url = reverse_lazy('usuarios:login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        current_site = get_current_site(self.request)
        dominio = get_current_site(self.request)

        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = token_activacion.make_token(user)

        message = render_to_string('confirmar_cuenta.html', {
            'user':user,
            'dominio':dominio,
            'uid': uid,
            'token': token
        })

        mail_subject = 'Activa tu cuenta'
        to_email = user.email
        email = EmailMessage(
            mail_subject, 
            message, 
            to=[to_email]
            )
        email.content_subtype = "html"
        email.send()

        return super().form_valid(form)


class ActivarCuenta(TemplateView):
    def get(self, request, *args, **kwargs):
        # context = self.get_context_data(**kwargs)

        try:
            uid = urlsafe_base64_decode(kwargs['uidb64'])
            token = kwargs['token']
            user = Usuario.objects.get(pk=uid) 
        except(TypeError, ValueError, Usuario.DoesNotExist):
            user = None
        
        if user is not None and token_activacion.check_token(user, token):
            user.is_active = True
            user.save()
            messages.success(self.request, 'Cuenta activada, ingresar datos')
        else:
            messages.error(self.request, 'Token inválido, contacta al administrador')

        return redirect('usuarios:login')
        

class Perfil(SuccessMessageMixin, UpdateView):
    template_name = 'perfil.html'
    model = Usuario
    form_class = PerfilForm
    success_url = reverse_lazy('usuarios:perfil')
    success_message = "El usuario %(first_name)s se actualizó con éxito"

    def get_object(self, queryset=None):
        pk = self.request.user.pk
        obj = Usuario.objects.get(pk=pk)
        return obj


    # def get_success_url(self):
    #     pk = self.kwargs.get(self.pk_url_kwarg)
    #     url = reverse_lazy('usuarios:perfil', kwargs={'pk': pk})
    #     return url