# Internship_Project_3

Docker container for a simple Python Flask application — run it locally.

## Application

A minimal [Flask](https://flask.palletsprojects.com/) web application with two endpoints:

| Endpoint  | Response                              |
|-----------|---------------------------------------|
| `/`       | HTML "Hello, World!" page             |
| `/health` | JSON `{"status": "ok"}` health check  |

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running

## Run with Docker Compose (recommended)

```bash
docker compose up --build
```

Then open <http://localhost:5000> in your browser.

To stop the container press `Ctrl+C`, then run:

```bash
docker compose down
```

## Run with Docker directly

```bash
# Build the image
docker build -t python-flask-app .

# Run the container
docker run -p 5000:5000 python-flask-app
```

Then open <http://localhost:5000> in your browser.

## Project structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies (Flask + Gunicorn)
├── Dockerfile          # Container image definition
├── docker-compose.yml  # Compose configuration for local development
└── README.md
```
