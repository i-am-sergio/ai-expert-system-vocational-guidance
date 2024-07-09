# Backend: System Expert Difuse

## Descripción

Este proyecto es un orientador vocacional basado en el código de Holland, utilizando un sistema experto con lógica difusa para recomendar o sugerir carreras que podrían interesarte.

El sistema evalúa las respuestas del usuario en diferentes categorías (Realista, Artístico, Investigativo, Social, Emprendedor y Convencional) y utiliza un sistema experto basado en lógica difusa para calcular recomendaciones personalizadas basadas en los patrones de respuesta.

## Instrucciones de ejecución

Para ejecutar la aplicación, sigue estos pasos:

1. **Instalar las dependencias:**

   ```
   pip install -r requirements.txt
   ```

   Asegúrate de que la versión máxima de Python sea 3.11.9 para evitar problemas de compatibilidad con las dependencias.

2. **Ejecutar la aplicación:**

   ```
   python app.py
   ```

   Esto iniciará el servidor Flask en el puerto 5000 por defecto.

## Endpoints y rutas para probar con Postman

### GET `/pregunta`

- **Descripción:** Devuelve la pregunta actual del diagnóstico.
- **Uso:** Realiza una solicitud GET a `/pregunta` para obtener la siguiente pregunta en el diagnóstico.
- **Ejemplo en Postman:** `GET http://localhost:5000/pregunta`

### POST `/respuesta`

- **Descripción:** Envia una respuesta al servidor para continuar con el diagnóstico.
- **Uso:** Realiza una solicitud POST a `/respuesta` con el siguiente cuerpo JSON:
  ```json
  {
    "answer": "si"
  }
  ```
  Donde `"si"` es la respuesta a la pregunta actual.
- **Ejemplo en Postman:** `POST http://localhost:5000/respuesta`

### POST `/nuevo_diagnostico`

- **Descripción:** Reinicia el diagnóstico, borrando las respuestas previas.
- **Uso:** Realiza una solicitud POST a `/nuevo_diagnostico` para comenzar un nuevo diagnóstico desde cero.
- **Ejemplo en Postman:** `POST http://localhost:5000/nuevo_diagnostico`

### POST `/register`

- **Descripción:** Registra un nuevo usuario en el sistema.
- **Uso:** Realiza una solicitud POST a `/register` con el siguiente cuerpo JSON:
  ```json
  {
    "username": "usuario",
    "password": "contraseña"
  }
  ```
- **Ejemplo en Postman:** `POST http://localhost:5000/register`

### POST `/login`

- **Descripción:** Inicia sesión con credenciales de usuario existentes.
- **Uso:** Realiza una solicitud POST a `/login` con el siguiente cuerpo JSON:
  ```json
  {
    "username": "usuario",
    "password": "contraseña"
  }
  ```
- **Ejemplo en Postman:** `POST http://localhost:5000/login`

### GET `/`

- **Descripción:** Página de inicio del sistema experto.
- **Uso:** Accede a `/` para recibir un mensaje de bienvenida y las instrucciones para comenzar.
- **Ejemplo en Postman:** `GET http://localhost:5000/`
