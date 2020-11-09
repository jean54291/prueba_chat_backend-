from django.db import models
from modulos.usuarios.models import Usuario

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    borrado = models.BooleanField(default=False)
    observaciones = models.CharField(max_length=5000, default='', null=True, blank=True, verbose_name="observaciones")
    notas = models.CharField(max_length=5000, default='', null=True, blank=True, verbose_name="notas")
    image = models.FileField(upload_to='uploads', null=True, blank=True)
    fecha_creacion = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    usuario = models.ForeignKey(Usuario,related_name="usuario", on_delete=models.CASCADE,null=True, blank=True, verbose_name="Persona")
