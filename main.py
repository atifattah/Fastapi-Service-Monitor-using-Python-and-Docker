import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_service_status():
    return {
        "service": "FastAPI Application",
        "status": "healthy",
        "uptime": "online",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="0.0.0.0")