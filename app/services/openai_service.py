from openai import OpenAI
from app.core.config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_content_calendar(plan: dict) -> list:
    prompt = f"""
You are a senior digital marketing strategist.

Create a monthly social media content calendar.

Return ONLY valid JSON.

Fields:
- publish_date
- topic
- ad_copy
- hashtags
- image_prompt

Plan:
{json.dumps(plan, indent=2)}
"""

    response = client.responses.create(
        model="gpt-4.1",
        input=prompt,
        max_output_tokens=1500
    )

    return response.output_text
