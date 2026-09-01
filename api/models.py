from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    class Meta:
        db_table = 'usuario'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username


class Proyecto(models.Model):
    nombre = models.CharField(max_length=150, verbose_name="Nombre")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="proyectos")

    def __str__(self):
        return self.nombre


class Tarea(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En progreso'),
        ('completada', 'Completada'),
    ]
    titulo = models.CharField(max_length=200, verbose_name="Título")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente', verbose_name="Estado")
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.titulo