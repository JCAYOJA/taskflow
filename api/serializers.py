from rest_framework import serializers
from .models import Proyecto, Tarea, Usuario  # 🚀 Cambiado para usar tu modelo personalizado de api/models.py

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario  # 🚀 Apunta a tu modelo personalizado
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

    def validate_proyecto(self, value):
        """
        Validación de seguridad: Evita que un usuario cree o edite una tarea
        asociándola a un proyecto que pertenece a otro usuario.
        """
        user = self.context['request'].user
        if value.usuario != user:
            raise serializers.ValidationError("No tienes permisos para interactuar con este proyecto.")
        return value
