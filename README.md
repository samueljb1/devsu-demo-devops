# Devsu Demo DevOps Project

DevOps Technical Challenge – Django + PostgreSQL + Kubernetes

📦 Project Overview

This is a demo project showcasing DevOps skills, including:

Dockerization of a Django web application.

CI/CD pipeline using GitHub Actions.

Deployment to Kubernetes with PostgreSQL backend.

Use of ConfigMaps, Secrets, Ingress, and HPA.

Bonus: IaC practices with structured and reusable Kubernetes manifests.

🚀 Technologies Used

Python 3.11 / Django

PostgreSQL

Docker / Docker Compose

GitHub Actions

Kubernetes (Docker Desktop)

Gunicorn

HPA (Horizontal Pod Autoscaler)

ConfigMap / Secret / Ingress

📁 Project Structure

├── app/                # Django app
├── Dockerfile          # Builds the image
├── docker-compose.yml  # Local dev/test
├── .github/workflows/  # CI/CD pipelines
│   └── main.yml
├── k8s/                # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── ingress.yaml
│   ├── configmap.yaml
│   ├── secret.yaml
│   └── hpa.yaml
├── screenshots/        # Images showing evidence of deployment

🔧 How to Run

1. Locally with Docker Compose

docker-compose up --build

2. In Kubernetes

kubectl apply -f k8s/

Ensure Kubernetes is enabled in Docker Desktop and Ingress is supported.

3. Access the App

kubectl get pods
kubectl logs <django-pod>

Then open http://localhost or http://django.local in your browser.

If you encounter a 404 error, ensure the Ingress and Service are configured properly. You may need to edit your hosts file to include:

127.0.0.1 django.local

⚙️ GitHub Actions

The CI/CD workflow includes:

Linting with flake8

Testing Django app

Building Docker image

Pushing to Docker Hub

Triggering Kubernetes deployment (manually or via kubectl)

All workflows are defined in .github/workflows/main.yml.

📊 Diagrams

1. Architecture Diagram



2. CI/CD Pipeline Diagram



📷 Screenshots

App running in browser

kubectl get pods showing Running

GitHub Actions pipeline passing

DockerHub image visible and tagged

🛠️ Troubleshooting

CrashLoopBackOff: Ensure the PostgreSQL container is running and the DB settings (ConfigMap/Secret) match the Django settings.

Ingress 404: Check service name and ingress host. Add domain to /etc/hosts.

Database errors: Confirm connectivity using psql, check logs with kubectl logs <postgres-pod>.

🔗 URLs to Include in Delivery

GitHub repo: https://github.com/samueljb1/devsu-demo-devops-final

DockerHub: https://hub.docker.com/r/samueljb1/devsu-django-app

App: http://localhost / http://django.local (see screenshots)

GitHub Actions: GitHub repo → Actions tab or screenshots in screenshots/

Prepared by: Samuel BlancoEmail: samuel_jb1@hotmail.comDate: May 2025

