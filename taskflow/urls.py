from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="TaskFlow API",
      default_version='v1',
      description="API para gestión de proyectos y tareas. Para autenticarse, inicie sesión o use los tokens de la API.",
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Panel de Administración
    path('admin/', admin.site.urls),
    
    # Autenticación JWT para la API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoints de la API REST
    path('api/', include('api.urls_api')),
    
    # Vistas del Frontend / Plantillas tradicionales (Login, Registro, etc.)
    path('', include('api.urls')),
    
    # Documentación interactiva de la API con Swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
