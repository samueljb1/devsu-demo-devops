FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies - like psycopg2
RUN apt-get update && apt-get install -y gcc libpq-dev curl && apt-get clean

# Copy and install dependencies first to use the cache correctly
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy code
COPY . .

ENV PYTHONPATH="/app"

# Healthcheck
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8000/api/hello/ || exit 1

# Create user without privileges
RUN adduser --disabled-password --no-create-home appuser
USER appuser

# RUN APP
CMD ["gunicorn", "demo.wsgi:application", "--bind", "0.0.0.0:8000"]


