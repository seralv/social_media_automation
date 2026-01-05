from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Social Media Automation",
    description="Social Media Automation with AI",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}
