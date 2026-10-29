# webActivityLeo - Guía Completa de la Aplicación Web Local

Este proyecto implementa la arquitectura multi-base de datos dentro de la carpeta `~/Descargas/webActivityLeo`.

---

## Cumplimiento de los 6 Requerimientos

1. **Frontend**: Aplicación SPA responsive creada con HTML5, Tailwind CSS y FontAwesome, accesible desde servidor web Nginx.
2. **Backend**: Servicio API REST desacoplado construido en Python con el framework **FastAPI** y servidor ASGI Uvicorn.
3. **Tres Bases de Datos**:
   * **MariaDB**: Gestión de la entidad `Actividades`.
   * **MySQL**: Gestión de la entidad `Alumnos`.
   * **PostgreSQL**: Gestión de la entidad `Profesores`.
   * **Redis**: Capa de caching y consolidación analítica.
4. **Contenedor de Despliegue**: Orquestación Docker Compose (`docker-compose.yml`) con 6 contenedores enlazados en red privada.
5. **CRUD Básico Completo**: Interfaz y API con operaciones de Crear, Leer, Actualizar y Eliminar independientes para cada base de datos.
6. **README.md**: Documentación exhaustiva con la arquitectura, tecnologías y guía de ejecución local en Visual Studio Code.

---

## Estructura de Directorios

```text
~/Descargas/webActivityLeo/
├── database/
│   ├── init_mariadb.sql
│   ├── init_mysql.sql
│   └── init_postgres.sql
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   └── index.html
├── docker-compose.yml
└── README.md
```

---

## Pasos para Desplegar desde la Terminal

Abre tu terminal en Linux/Mac/WSL y ejecuta los siguientes 6 pasos:

### 1. Detener el contenedor antiguo (si estaba activo)
```bash
docker rm -f activityleo_app
```

### 2. Crear las carpetas de `webActivityLeo` en Descargas
```bash
mkdir -p ~/Descargas/webActivityLeo/database ~/Descargas/webActivityLeo/backend ~/Descargas/webActivityLeo/frontend
```

### 3. Entrar a la nueva carpeta del proyecto
```bash
cd ~/Descargas/webActivityLeo
```

### 4. Abrir la carpeta en Visual Studio Code
```bash
code .
```

### 5. Iniciar la aplicación con Docker Compose
```bash
docker-compose up -d --build
```

### 6. Acceder a las direcciones web en el navegador
* **Frontend Dashboard**: `http://localhost:8080`
* **Swagger API Documentation (Backend Python)**: `http://localhost:8000/docs`