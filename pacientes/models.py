from django.db import models


class Estado(models.Model):
    nombre = models.CharField('Nombre del estado',max_length=120)
    def __str__(self):
        return self.nombre
    

class Municipio(models.Model):
    nombre = models.CharField('Nombre del municipio',max_length=120)
    estado = models.ForeignKey(Estado, verbose_name="Estado", on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre


class Paciente(models.Model):
    TIPO_SANGRE =  [
        ('A+', 'A positivo'),
        ('A-', 'A negativo'),
        ('O+', 'O positivo'),
    ]
    nombre = models.CharField(max_length=60)
    primerApellido = models.CharField('Apellido paterno',max_length=60)
    segundoApellido = models.CharField('Apellido materno', max_length=60, null=True, blank=True)
    numero_ss = models.CharField('Número de Seguro Social',max_length=20)
    fecha_nac = models.DateField('Fecha de nacimiento')
    tipo_sangre = models.CharField('Tipo de sangre', max_length=3, choices=TIPO_SANGRE)
    municipio = models.ForeignKey(Municipio, verbose_name='Municipio', on_delete=models.SET_NULL, null=True)
    estado = models.ForeignKey(Estado, verbose_name='Estado', on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.nombre + ' ' + self.primerApellido
    