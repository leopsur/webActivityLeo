# Documentación del CRUD Básico en webActivityLeo

El **CRUD** (Create, Read, Update, Delete) de la aplicación está totalmente integrado entre la interfaz de usuario **Frontend** (Nginx/JS) y la **API REST Backend** (Python FastAPI).

---

## 1. Mapeo de Rutas del Backend (`backend/app.py`)

A continuación se detallan las operaciones CRUD implementadas independientemente para cada una de las bases de datos:

### 📊 MariaDB — Entidad: Actividades
| Operación | Método HTTP | Ruta API | Código HTTP Esperado | Función Python |
| :--- | :--- | :--- | :--- | :--- |
| **Create** | `POST` | `/api/mariadb/actividades` | `200 OK` / `201 Created` | `create_actividad()` |
| **Read** | `GET` | `/api/mariadb/actividades` | `200 OK` | `get_actividades()` |
| **Update** | `PUT` | `/api/mariadb/actividades/{id}` | `200 OK` / `404 Not Found` | `update_actividad()` |
| **Delete** | `DELETE` | `/api/mariadb/actividades/{act_id}` | `200 OK` | `delete_actividad()` |

### 🎓 MySQL — Entidad: Alumnos
| Operación | Método HTTP | Ruta API | Código HTTP Esperado | Función Python |
| :--- | :--- | :--- | :--- | :--- |
| **Create** | `POST` | `/api/mysql/alumnos` | `200 OK` / `201 Created` | `create_alumno()` |
| **Read** | `GET` | `/api/mysql/alumnos` | `200 OK` | `get_alumnos()` |
| **Update** | `PUT` | `/api/mysql/alumnos/{id}` | `200 OK` / `404 Not Found` | `update_alumno()` |
| **Delete** | `DELETE` | `/api/mysql/alumnos/{alum_id}` | `200 OK` | `delete_alumno()` |

### 👨‍🏫 PostgreSQL — Entidad: Profesores
| Operación | Método HTTP | Ruta API | Código HTTP Esperado | Función Python |
| :--- | :--- | :--- | :--- | :--- |
| **Create** | `POST` | `/api/postgres/profesores` | `200 OK` / `201 Created` | `create_profesor()` |
| **Read** | `GET` | `/api/postgres/profesores` | `200 OK` | `get_profesores()` |
| **Update** | `PUT` | `/api/postgres/profesores/{id}` | `200 OK` / `404 Not Found` | `update_profesor()` |
| **Delete** | `DELETE` | `/api/postgres/profesores/{prof_id}` | `200 OK` | `delete_profesor()` |

---

## 2. Controladores en el Frontend (`frontend/index.html`)

El frontend consume la API REST usando la función asíncrona `fetch()` de JavaScript:

* **Lectura (`Read`):** `loadMariaDB()`, `loadMySQL()` y `loadPostgreSQL()` obtienen la lista actualizada de registros al cambiar de pestaña.
* **Creación y Edición (`Create / Update`):** La función `saveData(e)` captura los datos del formulario modal. Si existe un `id`, envía un `PUT` para actualizar; si no, envía un `POST` para crear.
* **Eliminación (`Delete`):** La función `deleteItem(target, endpoint, id)` solicita la eliminación enviando una petición HTTP `DELETE` previa confirmación del usuario.

---

## 3. Instrucciones para probar el CRUD

1. **Desde la Web (`http://localhost:8080`):**
   * Selecciona una pestaña (MariaDB, MySQL o PostgreSQL).
   * Pulsa en **"Nuevo Record"** para crear un registro.
   * Haz clic en el **icono de lápiz** para editar un registro existente.
   * Haz clic en el **icono de papelera** para eliminar un registro.

2. **Desde la Documentación de Swagger (`http://localhost:8000/docs`):**
   * Despliega cualquiera de los endpoints.
   * Haz clic en **"Try it out"** para ejecutar peticiones directamente contra el Backend en Python.