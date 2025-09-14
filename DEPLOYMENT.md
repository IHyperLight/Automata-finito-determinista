# Guía de Despliegue en Render

## Archivos configurados para Render:

### 1. requirements.txt
- Contiene todas las dependencias necesarias incluyendo gunicorn
- Compatible con el entorno de Python de Render

### 2. Procfile
- Especifica el comando de inicio: `gunicorn app:app`
- Render usa este archivo para saber cómo ejecutar la aplicación

### 3. render.yaml
- Configuración automática para Render
- Define el tipo de servicio, comandos de build y start
- Configura las variables de entorno necesarias

### 4. app.py (modificado)
- Usa variables de entorno para configuración
- PORT: Se obtiene del entorno (Render lo asigna automáticamente)
- SECRET_KEY: Se obtiene del entorno para seguridad
- FLASK_ENV: Se configura como 'production' en Render

### 5. start.py
- Script auxiliar para desarrollo local
- Usa waitress en Windows, gunicorn en Linux/Mac

## Variables de entorno en Render:
- FLASK_ENV: production
- SECRET_KEY: (se genera automáticamente)
- PORT: (Render lo asigna automáticamente)

## Pasos para desplegar:
1. Subir el código a GitHub
2. Crear cuenta en Render.com
3. Conectar el repositorio
4. Render detectará automáticamente render.yaml
5. ¡La aplicación estará disponible en unos minutos!

## Para desarrollo local:
- Windows: `python start.py` (usa waitress)
- Linux/Mac: `python start.py` (usa gunicorn)
- Alternativa: `python app.py` (usa Flask dev server)