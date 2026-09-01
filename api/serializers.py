from rest_framework import serializers
from .models import Proyecto, Tarea, Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email']


class ProyectoSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    class Meta:
        model = Proyecto
        fields = ['id', 'nombre', 'descripcion', 'usuario']


class TareaSerializer(serializers.ModelSerializer):
    proyecto_nombre = serializers.CharField(source='proyecto.nombre', read_only=True)
    class Meta:
        model = Tarea
        fields = ['id', 'titulo', 'estado', 'proyecto', 'proyecto_nombre']