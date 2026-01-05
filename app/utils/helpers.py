def parse_ai_json(ai_response: str) -> list:
    try:
        data = json.loads(ai_response)
        if not isinstance(data, list):
            raise ValueError("AI response is not a list")
        return data
    except Exception as e:
        print("Error parsing AI JSON:", e)
        # Devuelve lista vacía para que no rompa la API
        return []

# import json
#
#
# def parse_ai_json(ai_response: str) -> list:
#     try:
#         return json.loads(ai_response)
#     except json.JSONDecodeError:
#         raise ValueError("Invalid JSON returned by AI")
