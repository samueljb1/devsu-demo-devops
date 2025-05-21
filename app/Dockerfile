FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Instala dependencias del sistema necesarias para compilar paquetes como psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev curl && apt-get clean

# Copia e instala dependencias primero para usar la cache correctamente
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código
COPY . .

ENV PYTHONPATH="/app"

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/api/hello/ || exit 1

# Crear usuario sin privilegios
RUN adduser --disabled-password --no-create-home appuser
USER appuser

# Arrancar la app
CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]


