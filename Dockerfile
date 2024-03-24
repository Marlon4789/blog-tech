# Usa la imagen base de Python 3.12 en Alpine Linux
FROM python:3.12-alpine3.17

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos (requirements.txt) a /app
COPY requirements.txt requirements.txt

# Instala los requisitos de Django
RUN pip install -r requirements.txt

# Copia el resto del código de la aplicación a /app
COPY . .

# Define el comando predeterminado para ejecutar el servidor de desarrollo de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
