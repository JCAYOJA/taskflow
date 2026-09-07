from django.contrib import admin
from .models import Proyecto, Tarea, Usuario

# Si usas el Usuario personalizado (AbstractUser) debes registrarlo así:
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_staff')
    search_fields = ('username', 'email')

# Configuración avanzada para la entidad Proyecto
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    # Columnas que se verán en la tabla principal
    list_display = ('id', 'nombre', 'usuario')
    # Permite buscar proyectos por nombre o por el username del dueño
    search_fields = ('nombre', 'usuario__username')
    # Agrega un filtro lateral por usuario
    list_filter = ('usuario',)

# Configuración avanzada para la entidad Tarea
@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    # Columnas visibles
    list_display = ('id', 'titulo', 'proyecto', 'estado')
    # Permite buscar tareas por su título o por el nombre de su proyecto
    search_fields = ('titulo', 'proyecto__nombre')
    # Filtro lateral rápido para segmentar por estado o proyecto
    list_filter = ('estado', 'proyecto')
