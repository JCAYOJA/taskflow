TaskFlow — Gestión de Proyectos y Tareas
Sistema completo de gestión de proyectos y tareas desarrollado con Django y Django REST Framework, con autenticación JWT, interfaz web y API REST documentada.
✅ Características Principales
🔐 Registro e Inicio de Sesión de usuarios con validación
📁 CRUD completo de Proyectos (Crear, Listar, Editar, Eliminar)
✅ CRUD completo de Tareas vinculadas a proyectos
🔑 Autenticación JWT (Access Token + Refresh Token)
🌐 API REST con Django REST Framework
📚 Documentación automática con Swagger/OpenAPI
👤 Aislamiento por usuario: cada usuario gestiona solo sus propios recursos
🛡️ Protección de rutas, validación de formularios y protección CSRF
✅ Pruebas automatizadas y configuración de Logging
⚡ Optimización de consultas con select_related
🛠️ Tecnologías Utilizadas
Python 3.x
Django 6.1
Django REST Framework
SimpleJWT — Autenticación por tokens
DRF YASG — Documentación Swagger/OpenAPI
SQLite3 — Base de datos
python-dotenv — Variables de entorno
🚀 Pasos para Ejecutar el Proyecto
1. Crear y activar entorno virtual
bash
python -m venv venv

# En Windows:
venv\Scripts\activate

# En Linux / Mac:
source venv/bin/activate
2. Instalar dependencias
bash
pip install django djangorestframework djangorestframework-simplejwt drf-yasg python-dotenv
3. Crear archivo de variables de entorno
Crea un archivo .env al lado de manage.py:
env
SECRET_KEY=clave_secreta_de_tu_proyecto
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
4. Aplicar migraciones
bash
python manage.py makemigrations
python manage.py migrate
5. Crear usuario administrador
bash
python manage.py createsuperuser
Ingresa tu nombre de usuario, correo y contraseña cuando te lo solicite.
6. Iniciar el servidor
bash
python manage.py runserver
🌐 Direcciones Disponibles
Table
Ruta	Descripción
http://127.0.0.1:8000/	Página principal — Inicio de sesión
http://127.0.0.1:8000/registro/	Registro de nuevo usuario
http://127.0.0.1:8000/proyectos/	Gestión de proyectos
http://127.0.0.1:8000/tareas/	Gestión de tareas
http://127.0.0.1:8000/admin/	Panel de administración Django
http://127.0.0.1:8000/swagger/	📚 Documentación API Swagger
http://127.0.0.1:8000/api/token/	🔑 Obtener token JWT (POST)
http://127.0.0.1:8000/api/token/refresh/	🔑 Renovar token JWT (POST)
http://127.0.0.1:8000/api/proyectos/	API — Proyectos
http://127.0.0.1:8000/api/tareas/	API — Tareas
http://127.0.0.1:8000/api/tareas/pendientes/	API — Tareas pendientes
🔑 Uso de la API con Autenticación JWT
1. Obtener par de tokens
http
POST /api/token/
Content-Type: application/json

{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
Respuesta:
json
{
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
Access Token: Válido por 15 minutos → se usa para acceder a los endpoints protegidos
Refresh Token: Válido por 1 día → se usa para obtener un nuevo Access Token sin volver a iniciar sesión
2. Acceder a endpoints protegidos
Envía el Access Token en el encabezado de cada petición:
http
GET /api/proyectos/
Authorization: Bearer TU_ACCESS_TOKEN
3. Renovar Access Token
http
POST /api/token/refresh/
Content-Type: application/json

{ "refresh": "TU_REFRESH_TOKEN" }
✅ Ejecutar Pruebas Automatizadas
bash
python manage.py test api
Se ejecutan pruebas de:
✅ Obtención de token con credenciales válidas
✅ Acceso denegado sin token
✅ Creación de proyectos estando autenticado
📁 Estructura del Proyecto
plaintext
taskflow/
├── api/                              # Aplicación principal
│   ├── migrations/                  # Migraciones de base de datos
│   ├── templates/api/                # Plantillas HTML
│   │   ├── base.html
│   │   ├── registro.html
│   │   ├── login.html
│   │   ├── proyecto_lista.html
│   │   ├── proyecto_form.html
│   │   ├── proyecto_confirmar_eliminar.html
│   │   ├── tarea_lista.html
│   │   ├── tarea_form.html
│   │   └── tarea_confirmar_eliminar.html
│   ├── __init__.py
│   ├── admin.py                      # Registro en panel de administración
│   ├── apps.py
│   ├── forms.py                      # Formularios: Registro, Proyecto, Tarea
│   ├── models.py                     # Modelos: Usuario, Proyecto, Tarea
│   ├── serializers.py                # Serializadores de la API
│   ├── tests.py                      # Pruebas automatizadas
│   ├── urls.py                       # Rutas de vistas web
│   ├── urls_api.py                    # Rutas de API REST
│   ├── views.py                       # Vistas web
│   └── views_api.py                   # Vistas API REST
├── taskflow/                         # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py                    # Configuración global
│   ├── urls.py                        # Rutas principales
│   └── wsgi.py
├── .env                               # Variables de entorno
├── .gitignore
├── manage.py                          # Script de administración
└── README.md                          # Este archivo
🎯 Cumplimiento de Requisitos del Proyecto
Table
#	Requisito	Estado
1	CRUD de Proyectos y Tareas	✅ COMPLETO
2	Autenticación, registro y protección de rutas	✅ COMPLETO
3	Formularios, validación de datos, protección CSRF	✅ COMPLETO
4	API REST con Serializers, ModelViewSet y APIView	✅ COMPLETO
5	Autenticación JWT (Access + Refresh Tokens)	✅ COMPLETO
6	Seguridad, variables de entorno, Logging, optimización de consultas, pruebas	✅ COMPLETO
7	Documentación Swagger/OpenAPI + README.md	✅ COMPLETO



📋 TaskFlow — Gestión de Proyectos y Tareas

## 📄 Descripción del proyecto
Sistema de gestión de proyectos y tareas desarrollado con **Django** y **Django REST Framework**. Incluye registro y autenticación de usuarios, CRUD completo de proyectos y tareas, API REST con autenticación JWT, documentación Swagger/OpenAPI y aislamiento de recursos por usuario. Cada usuario solo puede ver y gestionar sus propios proyectos y tareas.

---

## ✅ Requisitos previos
- **Python 3.x** instalado
- Entorno virtual de Python (`venv`)
- Gestor de paquetes `pip`

---

## 📦 Instalación de dependencias
```bash
# Activar entorno virtual
venv\Scripts\activate      # Windows
# source venv/bin/activate  # Linux / Mac

# Instalar paquetes necesarios
pip install django djangorestframework djangorestframework-simplejwt drf-yasg python-dotenv
⚙️ Configuración de variables de entorno
Crear archivo .env
En la carpeta raíz del proyecto (al lado de manage.py), crear el archivo .env con el siguiente contenido:
env
SECRET_KEY=tu_clave_secreta_aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
Incluir .env en .gitignore
Para proteger datos sensibles, el archivo .env debe estar listado en .gitignore y NO debe subirse al repositorio. El archivo .gitignore debe contener:
plaintext
venv/
__pycache__/
*.pyc
*.env
.env
db.sqlite3
*.log
🗄️ Configuración de la base de datos
El proyecto utiliza SQLite3 por defecto, configurado automáticamente en settings.py. No se requiere instalación adicional.
📊 Ejecución de migraciones
bash
python manage.py makemigrations
python manage.py migrate
Esto crea las tablas en la base de datos: Usuario, Proyecto y Tarea.
👤 Creación del superusuario
bash
python manage.py createsuperuser
Sigue los pasos en pantalla para definir:
Nombre de usuario
Correo electrónico (opcional)
Contraseña
🚀 Ejecución del servidor de desarrollo
bash
python manage.py runserver
El servidor estará disponible en: http://127.0.0.1:8000/
🌐 Direcciones útiles
Página principal: http://127.0.0.1:8000/
Panel de administración: http://127.0.0.1:8000/admin/
Documentación API Swagger: http://127.0.0.1:8000/swagger/
Obtener token JWT: http://127.0.0.1:8000/api/token/
plaintext

---

## ✅ Verificación de puntos solicitados

| Elemento del enunciado | Incluido |
|---|---|
| Descripción del proyecto | ✅ |
| Requisitos previos | ✅ |
| Instalación de dependencias | ✅ |
| Configuración de variables de entorno (`.env`) | ✅ |
| `.env` incluido en `.gitignore` | ✅ |
| Configuración de la base de datos | ✅ |
| Ejecución de migraciones | ✅ |
| Creación del superusuario | ✅ |
| Ejecución del servidor de desarrollo | ✅ |






Autor: JCAYOJA
Versión: 1.0
Fecha: 31 de agosto de 2026