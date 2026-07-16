#  Gestión de Usuarios

API REST desarrollada con Flask y MySQL para PYME. Permite crear, consultar, actualizar y eliminar usuarios, con autenticación JWT, documentación Swagger .

# Tecnologías

- Python 3.11+
- Flask
- Flask-SQLAlchemy (ORM)
- Flask-Migrate (migraciones)
- Flask-JWT-Extended (autenticación)
- Flasgger (documentación Swagger/OpenAPI)
- MySQL

## Instalación

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd pyme
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv
venv\Scripts\Activate.ps1
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Crear la base de datos

Crea una base de datos vacía en MySQL:

```sql
CREATE DATABASE pyme;
```

### 5. Configurar la conexión

En `app.py`, ajusta la línea de conexión a tu base de datos si tu usuario o contraseña de MySQL son distintos:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/pyme"
```
## Migraciones

Este proyecto usa Flask-Migrate para gestionar los cambios en la base de datos.

### Inicializar migraciones (solo la primera vez)

```bash
flask db init
```

Esto crea la carpeta `migrations/` que guarda el historial de cambios del esquema. Ya está incluida en este repositorio, así que normalmente no necesitas correr este paso de nuevo.

### Crear una nueva migración

Cuando modifiques un modelo (por ejemplo, agregar una columna):

```bash
flask db migrate -m "descripcion del cambio"
```

Esto genera un archivo en `migrations/versions/` con los cambios detectados.

### Aplicar las migraciones

```bash
flask db upgrade
```

Este comando ejecuta los cambios pendientes contra la base de datos, creando o actualizando las tablas necesarias.

### Ejecutar el proyecto

Con la base de datos migrada, levanta el servidor:

```bash
python app.py
```

El servidor estará disponible en `http://127.0.0.1:5000`.

## Autenticación

El endpoint `DELETE /users/{id}` requiere un token JWT. Para obtenerlo, primero inicia sesión:

**Credenciales de prueba:**
- usuario: `admin`
- contraseña: `admin123`

El login devuelve un `access_token` que debe enviarse en el header `Authorization` con el prefijo `Bearer` en las peticiones protegidas.
## Documentación interactiva (Swagger)

Con el servidor corriendo, puedes explorar y probar todos los endpoints desde:
http://127.0.0.1:5000/docs/
## Ejemplos con CURL

### Login (obtener token)

```bash
curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d "{\"usuario\": \"admin\", \"contrasena\": \"admin123\"}"
```

### Crear usuario

```bash
curl -X POST http://127.0.0.1:5000/users -H "Content-Type: application/json" -d "{\"nombre\": \"Kairo\", \"correo\": \"kairo@example.com\", \"telefono\": \"5512345678\"}"
```

### Obtener listado de usuarios

```bash
curl -X GET http://127.0.0.1:5000/users
```

### Obtener usuario por ID

```bash
curl -X GET http://127.0.0.1:5000/users/1
```

### Actualizar usuario

```bash
curl -X PUT http://127.0.0.1:5000/users/1 -H "Content-Type: application/json" -d "{\"telefono\": \"5599999999\"}"
```

### Eliminar usuario (requiere token JWT)

```bash
curl -X DELETE http://127.0.0.1:5000/users/1 -H "Authorization: Bearer TU_TOKEN_AQUI"
```