from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views_api import ProyectoViewSet, TareaViewSet, TareasPendientesAPIView

router = DefaultRouter()
router.register(r'proyectos', ProyectoViewSet)
router.register(r'tareas', TareaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tareas/pendientes/', TareasPendientesAPIView.as_view(), name='tareas-pendientes'),
]