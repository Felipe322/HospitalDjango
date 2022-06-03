from .models import Paciente
from django.forms import ModelForm, TextInput, Select, DateInput


class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = ('nombre','primerApellido','segundoApellido',
            'numero_ss','fecha_nac','tipo_sangre','estado','municipio')

        widgets = {
                'nombre':TextInput(attrs={'class':'form-control'}),
                'primerApellido':TextInput(attrs={'class':'form-control'}),
                'segundoApellido':TextInput(attrs={'class':'form-control'}),
                'numero_ss':TextInput(attrs={'class':'form-control'}),
                'fecha_nac':DateInput(attrs={'class':'form-control'}),
                'tipo_sangre':Select(attrs={'class':'form-control'}),
                'estado':Select(attrs={'class':'form-control'}),
                'municipio':Select(attrs={'class':'form-control'}),
        }
