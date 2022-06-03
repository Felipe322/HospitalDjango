from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator, RegexValidator


imagen_png = FileExtensionValidator(allowed_extensions=['png'],message="Sólo se permiten imágenes PNG")

rfc_validador = RegexValidator(
    regex='^([A-ZÑ&]{3,4}) ?(?:- ?)?(\d{2}(?:0[1-9]|1[0-2])(?:0[1-9]|[12]\d|3[01])) ?(?:- ?)?([A-Z\d]{2})([A\d])$',
    message='El RFC no tiene un formato válido',
    code='rfc_invalido'
)

class Usuario(User):
    rfc = models.CharField('R.F.C.', max_length=13, validators=[rfc_validador])
    foto = models.ImageField('Foto', upload_to='perfil',null=True, blank=True, validators=[imagen_png])

    def __str__(self):
        return self.username
    

