from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/nuevo/', views.crear_proyecto, name='crear_proyecto'),
    path('proyectos/<int:pk>/editar/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/<int:pk>/eliminar/', views.eliminar_proyecto, name='eliminar_proyecto'),
    path('tareas/', views.lista_tareas, name='lista_tareas'),
    path('tareas/nueva/', views.crear_tarea, name='crear_tarea'),
    path('tareas/<int:pk>/editar/', views.editar_tarea, name='editar_tarea'),
    path('tareas/<int:pk>/eliminar/', views.eliminar_tarea, name='eliminar_tarea'),
]