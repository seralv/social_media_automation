from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.publication import MonthlyPlan
from app.services.openai_service import generate_content_calendar
from app.utils.helpers import parse_ai_json
from app.db.database import SessionLocal
from app.db.crud import create_posts

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/plan")
def create_monthly_plan(plan: MonthlyPlan, db: Session = Depends(get_db)):
    ai_calendar_raw = generate_content_calendar(plan.dict())
    calendar = parse_ai_json(ai_calendar_raw)

    for platform in plan.platforms:
        create_posts(
            db = db,
            company_name = plan.company_name,
            platform = platform,
            calendar = calendar
        )

    return {
        "message": "Content calendar stored successfully",
        "total_posts": len(calendar) * len(plan.platforms)
    }
