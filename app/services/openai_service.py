# When you have credits in OpenAI uncomment and use the commented below, and comment the code here

import json

USE_MOCK_AI = True  # 🔥 change to False when you have credits


def generate_content_calendar(plan: dict) -> str:
    if USE_MOCK_AI:
        return json.dumps([
            {
                "company_name": "La Jefa",
                "platforms": ["instagram", "facebook"],
                "month": "2026-04",
                "total_posts": 12,
                "frequency": "3 per week",
                "product": "Mexican food with any meat",
                "goal": "promotional",
                "style": "colorful, appetizing, tasty",
                "target_audience": "Young people 18-30",
                "call_to_action": "Visit us and make your life happy!"
            }
        ])



# Uncomment this code whe you have OpenAI credits
# from openai import OpenAI
# from app.core.config import OPENAI_API_KEY
# import json
#
# client = OpenAI(api_key=OPENAI_API_KEY)
#
#
# def generate_content_calendar(plan: dict) -> list:
#     prompt = f"""
# You are a senior digital marketing strategist.
#
# Create a monthly social media content calendar.
#
# Return ONLY valid JSON.
#
# Fields:
# - publish_date
# - topic
# - ad_copy
# - hashtags
# - image_prompt
#
# Plan:
# {json.dumps(plan, indent=2)}
# """
#
#     response = client.responses.create(
#         model="gpt-4.1",
#         input=prompt,
#         max_output_tokens=1500
#     )
#
#     return response.output_text
