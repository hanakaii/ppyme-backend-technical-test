<p align="center">
  <img src="https://i.ibb.co/WvbPJDNW/PPYME.webp" width="250" alt="PPYME Logo">
</p>

<h1 align="center">
🚀 Examen Técnico — Desarrollador Backend Python
</h1>

<h3 align="center">
API REST + Swagger + Flask + Base de Datos
</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/Swagger-OpenAPI-green?style=for-the-badge&logo=swagger">
  <img src="https://img.shields.io/badge/Database-SQL%20%7C%20NoSQL-orange?style=for-the-badge">
</p>

---

# 📌 Descripción

Bienvenido al proceso técnico de selección de **PPYME**.

El objetivo de esta prueba es evaluar conocimientos en desarrollo backend utilizando **Python** y **Flask**, aplicando buenas prácticas de arquitectura de software, documentación de APIs, manejo de bases de datos y control de versiones.

El candidato deberá desarrollar una:

- ✅ API REST profesional
- ✅ Funcional
- ✅ Documentada
- ✅ Bien estructurada

---

# 🛠️ Tecnologías Requeridas

## ⚙️ Backend

- Python 3.11+
- Flask

## 🗄️ Base de Datos

El candidato puede elegir cualquiera de las siguientes opciones:

- PostgreSQL
- MySQL
- MariaDB
- SQLite
- MongoDB *(solo si justifica correctamente la arquitectura)*

---

# 📋 Requerimientos Técnicos

La solución deberá incluir obligatoriamente:

- ✅ API REST funcional
- ✅ Documentación Swagger/OpenAPI
- ✅ Uso de Flask-Migrate
- ✅ Conexión a base de datos
- ✅ Arquitectura limpia y estructurada
- ✅ Validaciones
- ✅ Manejo de errores
- ✅ Archivo README completo
- ✅ Ejemplos CURL documentados por el candidato
- ✅ Repositorio Git

---

# 📦 Módulo a Desarrollar

## 👤 Sistema de Gestión de Usuarios

La API deberá permitir las siguientes operaciones:

| Método | Endpoint | Descripción |
|---|---|---|
| POST | `/users` | Crear usuario |
| GET | `/users` | Obtener listado de usuarios |
| GET | `/users/{id}` | Obtener usuario por ID |
| PUT | `/users/{id}` | Actualizar usuario |
| DELETE | `/users/{id}` | Eliminar usuario |

---

# 🧱 Estructura Recomendada

El proyecto deberá mantener una estructura profesional y organizada.

```bash
project/
│
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── schemas/
│   ├── config/
│   └── extensions/
│
├── migrations/
├── tests/
├── run.py
├── requirements.txt
├── .env
├── README.md
└── .gitignore
```

---

# 🧾 Requerimientos Funcionales

## 👥 Modelo Usuario

El modelo deberá contener al menos los siguientes campos:

| Campo | Tipo |
|---|---|
| id | Integer / UUID |
| nombre | String |
| correo | String |
| telefono | String |
| fecha_creacion | DateTime |

---

# ✅ Validaciones

La API deberá validar:

- Correos duplicados
- Campos obligatorios
- Tipos de datos
- Longitudes mínimas y máximas
- Manejo correcto de errores HTTP
- Respuestas JSON consistentes

---

# 📚 Swagger / OpenAPI

La documentación Swagger deberá incluir:

- ✅ Endpoints
- ✅ Request Body
- ✅ Responses
- ✅ Códigos HTTP
- ✅ Ejemplos

La documentación deberá estar disponible desde:

```bash
/docs
```

Puede utilizar cualquiera de las siguientes librerías:

- flasgger
- flask-restx
- flask-smorest
- connexion
- cualquier librería compatible con OpenAPI

---

# 🗃️ Migraciones

El proyecto deberá implementar:

```bash
Flask-Migrate
```

El candidato deberá documentar en el README:

- Proceso de inicialización
- Creación de migraciones
- Ejecución de migraciones
- Actualización de base de datos

---

# 🌐 CURLs Obligatorios

El candidato deberá agregar ejemplos funcionales de CURL para:

- Crear usuario
- Obtener usuarios
- Obtener usuario por ID
- Actualizar usuario
- Eliminar usuario

---

# 🔀 Requerimientos de Git

El repositorio deberá contener:

- ✅ Commits claros y descriptivos
- ✅ Uso correcto de `.gitignore`
- ✅ README completo
- ✅ Código organizado
- ✅ Historial limpio y profesional

---

# ⭐ Puntos Extras

Se considerará un plus si el candidato implementa:

- 🐳 Docker
- 🐳 Docker Compose
- 🔐 JWT Authentication
- 📄 Variables de entorno
- 📑 Paginación
- 🔎 Filtros
- 🧪 Testing
- 📜 Logging
- 🏗️ Arquitectura por capas
- 🧩 Repository Pattern
- ⚡ CI/CD

---

# 📊 Criterios de Evaluación

| Criterio | Ponderación |
|---|---|
| 🧱 Arquitectura del proyecto | 20% |
| 🧹 Calidad del código | 20% |
| ⚙️ Funcionamiento de la API | 20% |
| 📚 Swagger/OpenAPI | 15% |
| 🗄️ Base de datos y migraciones | 15% |
| 📝 README y documentación | 10% |

---

# 📤 Entregables

El candidato deberá entregar:

- ✅ URL del repositorio Git
- ✅ README completo con instrucciones de instalación
- ✅ Código fuente funcional

---

# ⏳ Tiempo Estimado

```txt
4 a 8 horas
```

---

# ⚠️ Consideraciones

- El proyecto debe ser desarrollado completamente por el candidato.
- Se evaluará la claridad del código y las decisiones técnicas.
- El proyecto debe poder ejecutarse localmente sin problemas.
- El código debe reflejar buenas prácticas de desarrollo backend.
- No se permite copiar soluciones completas de internet.

---

# 🎯 Resultado Esperado

Una API REST profesional, documentada, estructurada y lista para producción.

---

# 🚀 ¡Éxito!

Asegúrate de entregar una solución:

- ✔️ Limpia
- ✔️ Organizada
- ✔️ Escalable
- ✔️ Bien documentada

Valoramos tanto el funcionamiento como la calidad del código y la estructura del proyecto.
