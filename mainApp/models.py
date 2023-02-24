from django.db import models
from AppUsuarios import models as modelosUsuarios

# Create your models here.

class Docente(modelosUsuarios.Persona):
        profesion = models.CharField(max_length = 50)


class Curso(models.Model):
        fecha = models.DateField()
        periodo = models.IntegerField()

class Clase(models.Model):
        hora_inicio = models.TimeField()
        hora_fin = models.TimeField()
        aula = models.TextField()

class Materia(models.Model):
        nombre_materia = models.TextField()

class estadoAsistencia(models.Model):
        estado = models.BooleanField()

class Asistencia(estadoAsistencia):
        descripcion =  models.TextChoices
