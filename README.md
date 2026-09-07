# TaskFlow — Gestión de Proyectos y Tareas

Sistema completo de gestión de proyectos y tareas desarrollado con **Django 6.1** y **Django REST Framework**, con autenticación JWT, interfaz web y API REST documentada.

---

## ✅ Características Principales
* **Autenticación segura:** Registro e inicio de sesión con validación de formularios, protección CSRF y aislamiento por usuario (cada usuario gestiona solo sus propios recursos).
* **Gestión total (CRUD):** Control completo de Proyectos y Tareas vinculadas.
* **API REST con JWT:** Autenticación mediante tokens de acceso (`Access Token`) y de renovación (`Refresh Token`).
* **Documentación automática:** API completamente documentada con Swagger/OpenAPI.
* **Calidad de código:** Pruebas automatizadas, logs configurados y políticas de intercambio de recursos cruzados (**CORS**) habilitadas.

---

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Framework principal:** Django 6.1 & Django REST Framework
* **Autenticación:** SimpleJWT
* **Documentación:** DRF YASG (Swagger)
* **Políticas CORS:** Django CORS Headers
* **Base de datos:** SQLite3
* **Configuración:** Python-dotenv

---

## 🚀 Pasos para Ejecutar el Proyecto

### 1. Clonar el repositorio y preparar el entorno
```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual (Windows)
venv\Scripts\activate

# Activar entorno virtual (Linux / Mac)
source venv/bin/activate

# Instalar dependencias necesarias
pip install django djangorestframework djangorestframework-simplejwt drf-yasg django-cors-headers python-dotenv
```

### 2. Configurar variables de entorno
Crea un archivo llamado `.env` en la raíz del proyecto (al lado de `manage.py`) con la siguiente estructura:
```env
SECRET_KEY=clave_secreta_de_tu_proyecto
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```
*(Nota: Asegúrate de que tu `.gitignore` incluya este archivo `.env`, la base de datos `db.sqlite3` y la carpeta `venv/`)*.

### 3. Inicializar la base de datos y el servidor
```bash
# Aplicar migraciones
python manage.py makemigrations api
python manage.py migrate

# Crear usuario administrador (Superusuario)
python manage.py createsuperuser

# Iniciar servidor de desarrollo
python manage.py runserver
```

---

## 🌐 Direcciones Disponibles

| Ruta | Descripción |
| :--- | :--- |
| `http://127.0.0.1:8000/` | Página principal / Redirección automática |
| `http://127.0.0` | Inicio de sesión (Web) |
| `http://127.0.0.1:8000/registro/` | Registro de nuevo usuario (Web) |
| `http://127.0.0.1:8000/proyectos/` | Panel de gestión de proyectos (Web) |
| `http://127.0.0.1:8000/tareas/` | Panel de gestión de tareas (Web) |
| `http://127.0.0.1:8000/admin/` | Panel de administración de Django |
| `http://127.0.0.1:8000/swagger/` | 📚 Documentación de la API con Swagger |
| `http://127.0.0.1:8000/api/token/` | 🔑 Obtener token JWT (POST) |
| `http://127.0.0.1:8000/api/token/refresh/` | 🔑 Renovar token JWT (POST) |
| `http://127.0.0.1:8000/api/proyectos/` | API REST — Endpoints de Proyectos |
| `http://127.0.0.1:8000/api/tareas/` | API REST — Endpoints de Tareas |
| `http://127.0.0` | 🚀 API REST — Endpoint Personalizado de Tareas Pendientes |

---

## 🔑 Uso básico de la API REST

### 1. Autenticación (POST `/api/token/`)
Envía tus credenciales en formato JSON:
```json
{
  "username": "tu_usuario",
  "password": "tu_contraseña"
}
```
Recibirás un `access` token (válido por 15 minutos) y un `refresh` token (válido por 1 día).

### 2. Consumir endpoints protegidos
Envía el token en las cabeceras HTTP de tus peticiones:
```http
Authorization: Bearer TU_ACCESS_TOKEN
```

---

## ✅ Pruebas Automatizadas
Para verificar el correcto funcionamiento del sistema de autenticación y flujos de la API, ejecuta:
```bash
python manage.py test api
```

---

## 📁 Estructura Principal del Proyecto
```plaintext
taskflow/
├── api/                    # Aplicación principal (Vistas, Modelos, Serializers y Tests)
│   ├── templates/api/      # Plantillas de la interfaz Web
│   ├── urls_api.py         # Rutas específicas de la API REST
│   └── urls.py             # Rutas específicas de la interfaz Web
├── taskflow/               # Configuración global del proyecto Django (Settings)
├── .env                    # Variables de entorno locales (Ignorado en Git)
├── .gitignore              # Archivos excluidos del control de versiones
├── manage.py               # Gestor de comandos de Django
└── README.md               # Este archivo
```

---
**Autor:** JCAYOJA  
**Versión:** 1.0  
**Fecha:** 6 de septiembre de 2026
`

---
**Autor:** JCAYOJA  
**Versión:** 1.0  
**Fecha:** 31 de agosto de 2026