from fastapi import APIRouter
from app.models.publication import MonthlyPlan
from app.services.openai_service import generate_content_calendar

router = APIRouter()


@router.post("/plan")
def create_monthly_plan(plan: MonthlyPlan):
    calendar = generate_content_calendar(plan.dict())
    return {
        "message": "Monthly plan received successfully",
        "data": plan
    }
