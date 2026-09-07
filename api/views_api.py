from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Proyecto, Tarea
from .serializers import ProyectoSerializer, TareaSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer
    permission_classes = [IsAuthenticated]
    queryset = Proyecto.objects.all()

    def get_queryset(self):
        # 🚀 Control para Swagger: Si la librería está autogenerando la documentación, 
        # intercepta la petición y devuelve un QuerySet vacío para evitar evaluar el AnonymousUser.
        if getattr(self, 'swagger_fake_view', False):
            return Proyecto.objects.none()
            
        return Proyecto.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer
    permission_classes = [IsAuthenticated]
    queryset = Tarea.objects.all()

    def get_queryset(self):
        # 🚀 Control para Swagger: Evita que el servidor colapse al intentar leer
        # el atributo 'self.request.user' cuando no hay una sesión activa de API.
        if getattr(self, 'swagger_fake_view', False):
            return Tarea.objects.none()
            
        return Tarea.objects.filter(proyecto__usuario=self.request.user)


class TareasPendientesAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        tareas = Tarea.objects.filter(estado='pendiente', proyecto__usuario=request.user)
        serializer = TareaSerializer(tareas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
