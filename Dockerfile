FROM python:3.9-slim

WORKDIR /app-root

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos TODO el contenido actual (incluyendo la carpeta app/)
COPY . .

# Exponer el puerto
EXPOSE 5000

# Comando para correr: python app/main.py
CMD ["python", "app/main.py"]