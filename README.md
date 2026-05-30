Documentación del Sistema
Sistema de Gestión de Citas – Clínica Dental
1. Descripción del sistema

Este sistema es una aplicación web para la gestión de citas de una clínica dental. Permite a los pacientes agendar citas de manera digital, almacenarlas en una base de datos y consultarlas posteriormente.

El sistema incluye:

-Registro de citas
-Visualización de citas
-Eliminación de citas
-Validación de datos del usuario
-Envío de confirmación por correo electrónico

El objetivo es digitalizar el proceso de agendamiento de citas para hacerlo más rápido, ordenado y accesible.

2. Tecnologías usadas

Frontend
-Vue.js (Vite)
-JavaScript
-HTML5
-CSS3
-Fetch API

Backend
-Python
-Flask
-Flask-CORS
-Flask-Mail
-Gunicorn (para producción)

Base de datos
-MySQL (Aiven Cloud)

Herramientas adicionales
-dotenv (variables de entorno)
-MySQL Connector Python

3. Arquitectura del sistema

El sistema sigue una arquitectura cliente-servidor:

Frontend (Cliente)
Vue.js
Envía solicitudes HTTP (fetch)
Muestra datos al usuario

Backend (Servidor API REST)
Flask
Procesa solicitudes
Valida datos
Conecta con la base de datos
Envía correos
Base de datos (Aiven MySQL)
Almacena las citas
Responde consultas del backend
Flujo del sistema:

Usuario → Vue.js → Flask API → MySQL (Aiven) → Flask → Vue.js

4. Endpoints del sistema
4.1 Obtener citas
GET /citas
Descripción:

Devuelve todas las citas registradas.

Respuesta:
[
  {
    "id": 1,
    "nombre_paciente": "Juan Perez",
    "telefono": "1234567890",
    "correo": "correo@gmail.com",
    "fecha": "2026-05-30",
    "hora": "10:00",
    "servicio": "Limpieza Dental"
  }
]
4.2 Crear cita
POST /citas
Descripción:

Registra una nueva cita.

Body JSON:
{
  "nombre": "Juan Perez",
  "telefono": "1234567890",
  "correo": "correo@gmail.com",
  "fecha": "2026-05-30",
  "hora": "10:00",
  "servicio": "Limpieza Dental"
}
4.3 Eliminar cita
DELETE /citas/<id>
Descripción:

Elimina una cita por su ID.

5. Arquitectura de base de datos
Tabla: citas
Campo	Tipo	Descripción
id	INT PK AI	Identificador único
nombre_paciente	VARCHAR	Nombre del paciente
telefono	VARCHAR	Teléfono
correo	VARCHAR	Email
fecha	DATE	Fecha de la cita
hora	TIME	Hora de la cita
servicio	VARCHAR	Tipo de servicio
fecha_registro	TIMESTAMP	Fecha de creación

6. URLs del sistema
Frontend (Vue en local o deploy)
http://localhost:5173
Backend (Render)
https://proyecto-final-danna-y-leonel.onrender.com

Endpoints API
GET    /citas
POST   /citas
DELETE /citas/<id>
