# Fastapi-Service-Monitor-using-Python-and-Docker
A containerized FastAPI microservice exposing a robust service monitoring and health status endpoint with version tracking.


# 📡 FastAPI Service Status API

A professional, Dockerized FastAPI microservice exposing a health check and service status endpoint. Ideal for monitoring setups, microservice environments, and application diagnostics.

---

## 🔍 Overview

This FastAPI application provides a structured JSON response at the root (`/`) endpoint, delivering real-time service status, version, and uptime details.

### 🧪 Example Response

```json
GET /
→ {
  "service": "FastAPI Application",
  "status": "healthy",
  "uptime": "online",
  "version": "1.0.0"
}
```

---

## ✨ Features

- ✅ Health check and uptime verification
- 📦 Lightweight FastAPI application
- 🚀 Fully containerized using Docker
- 📜 Versioned metadata returned at root endpoint

---

## 🛠️ Requirements

- ✅ Python 3.8+ (for local testing)
- 🐳 Docker installed (for containerization)
- 🧰 Optional: `curl` or a browser for quick checks

---

## ▶️ How to Use

### 🔧 Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python main.py
   ```

3. Test it:
   ```bash
   curl http://localhost:8000
   ```

---

## 🐳 Run with Docker

### Step 1: Build the Docker image

```bash
docker build -t fastapi-service-status-api .
```

### Step 2: Run the container

```bash
docker run -p 8000:8000 fastapi-service-status-api
```

Now visit [http://localhost:8000](http://localhost:8000) or use `curl` to verify service status.

---

## 📁 File Structure

```
.
├── Dockerfile          # Container configuration
├── main.py             # FastAPI application
└── requirements.txt    # Dependencies
```

---

## 📜 Dockerfile Overview

```dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

EXPOSE 8000

CMD ["python", "main.py"]
```

---

## 🧠 Use Cases

- Health check endpoint for load balancers and monitoring systems
- Microservice diagnostics and introspection
- Lightweight template for production-ready FastAPI APIs

---

## 🚀 Quickstart

```bash
docker build -t fastapi-service-status-api .
docker run -p 8000:8000 fastapi-service-status-api
curl http://localhost:8000
```

---

## 📄 License

MIT License – free to use, modify, and distribute.
