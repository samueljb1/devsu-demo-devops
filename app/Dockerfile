# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy contents from host's app/ to container's /app/
COPY . /app/

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port used by Gunicorn
EXPOSE 8000

# Set PYTHONPATH in case Django project needs it
ENV PYTHONPATH=/app

# Start Gunicorn using the correct Django project name ("demo")
CMD ["gunicorn", "--chdir", ".", "--bind", "0.0.0.0:8000", "demo.wsgi:application"]

