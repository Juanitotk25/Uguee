from django.db import models
from instituciones.models import Institucion

class Usuario(models.Model):
    uid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=50)
    celular = models.IntegerField()
    contraseña = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    instid = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False, help_text="¿Ha sido aprobado por la institución?")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class UsuarioType(models.Model):
    uid = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
    tipo = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.uid.nombre} - {self.tipo}"

class Documento(models.Model):
    uid = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=150)
    url = models.URLField(max_length=300, blank=True, null=True)  # URL pública del archivo

    class Meta:
        unique_together = ('uid', 'tipo', 'url')

    def __str__(self):
        return f"{self.uid.nombre} - {self.tipo}"
