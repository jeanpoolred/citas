# API de Citas

Esta es una API para gestionar citas médicas. Permite crear, obtener, actualizar y eliminar citas.

## Endpoints

### Obtener Todas las Citas

**URL:** `/appointments`

**Método:** `GET`

**Autenticación:** Requerida (usuario: `admin`, contraseña: `secret`)

**Respuesta Exitosa:**

- **Código:** 200 OK
- **Contenido:**
  ```json
  [
      {
          "id": 1,
          "patient_name": "John Doe",
          "doctor_name": "Dr. Smith",
          "appointment_time": "2024-08-01T10:00:00",
          "description": "Routine checkup"
      }
  ]
