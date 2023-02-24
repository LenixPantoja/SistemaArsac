from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Persona(models.Model):
    user = models.OneToOneField(User, verbose_name="Usuario", on_delete=models.CASCADE)
    cedula = models.CharField(max_length=50, verbose_name="Cedula")
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length = 50)
    telefono = models.CharField(max_length = 100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        return str(self.cedula)


