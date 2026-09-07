from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ProyectoViewSet, TareaViewSet, TareasPendientesAPIView

router = DefaultRouter()
# ✅ Mantener 'basename' debido al queryset dinámico de tus vistas
router.register(r'proyectos', ProyectoViewSet, basename='proyecto')
router.register(r'tareas', TareaViewSet, basename='tarea')

urlpatterns = [
    # 🚀 CORRECCIÓN: Ponemos la ruta fija ARRIBA para que Django la capture antes que las rutas dinámicas del router
    path('tareas/pendientes/', TareasPendientesAPIView.as_view(), name='tareas-pendientes'),
    path('', include(router.urls)),
]
