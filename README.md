# code-notebook-app
Plataforma de aprendizaje de Python/C++ con enfoque en escritura manual y entrevistas.

## Arquitectura (Clean Architecture)

El backend está desarrollado en Python usando **FastAPI** y sigue los principios de Clean Architecture para garantizar un código limpio, mantenible y escalable.

### Estructura de Directorios

```
app/
├── api/             # Routers de FastAPI y endpoints.
│   ├── endpoints/   # Rutas organizadas por dominio (lessons, exercises, users).
│   └── api.py       # Router principal que agrupa todos los sub-routers.
├── core/            # Configuraciones, seguridad y utilidades transversales.
├── db/              # Configuración de base de datos y modelo Base de SQLAlchemy.
├── models/          # Entidades de base de datos (SQLAlchemy).
├── schemas/         # Modelos de validación (Pydantic) para peticiones y respuestas.
├── services/        # Lógica de negocio de la aplicación.
└── main.py          # Punto de entrada de la aplicación FastAPI (en la raíz).
```

### Modelo de Datos Inicial

- **BoardLesson**: Representa las "Lecciones de Pizarra", con teoría, tips de sintaxis, diagramas y lenguaje.
- **TerminalExercise**: Representa los "Ejercicios de Terminal", asociados a una lección. Incluye problemas, código inicial y salidas esperadas (enfocados en entrevistas).
- **User**: Usuarios del sistema.
- **HabitTracking**: Seguimiento de hábitos y rachas de los usuarios, contabilizando lecciones y ejercicios completados diariamente.

### Endpoints REST Básicos

La API está versionada bajo el prefijo `/api/v1/`.

**Lecciones de Pizarra (`/lessons`)**
- `GET /lessons`: Obtiene la lista de lecciones disponibles.
- `POST /lessons`: Crea una nueva lección.
- `GET /lessons/{lesson_id}`: Obtiene los detalles de una lección específica.

**Ejercicios de Terminal (`/exercises`)**
- `GET /exercises`: Obtiene ejercicios de terminal.
- `POST /exercises`: Crea un nuevo ejercicio.
- `GET /exercises/{exercise_id}`: Obtiene un ejercicio específico por ID.

**Usuarios y Seguimiento de Hábitos (`/users`)**
- `POST /users`: Registra un nuevo usuario.
- `GET /users/{user_id}`: Perfil del usuario.
- `GET /users/{user_id}/habits`: Historial de rachas y hábitos de un usuario.
- `POST /users/{user_id}/habits`: Registra actividad diaria para el seguimiento de hábitos.
