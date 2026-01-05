from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Social Media Automation",
    description="Social Media Automatization with AI",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}
