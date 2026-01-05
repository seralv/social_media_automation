from pydantic import BaseModel, Field
from typing import List


class MonthlyPlan(BaseModel):
    company_name: str = Field(..., example="El Fuego Taqueria")
    platforms: List[str] = Field(..., example=["instagram", "facebook"])
    month: str = Field(..., example="2026-03")
    total_posts: int = Field(..., gt=0, example=12)
    frequency: str = Field(..., example="3 per week")
    product: str = Field(..., example="Mexican tacos")
    goal: str = Field(..., example="promotional")
    style: str = Field(..., example="colorful, appetizing")
    target_audience: str = Field(..., example="Young people 18-30")
    call_to_action: str = Field(..., example="Visit us today")
