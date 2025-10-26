import os
import subprocess as sp; sp.call('cls',shell=True)
from google import genai
from google.genai import types


gemini_api = os.environ.get("GEMINI_API_KEY")
print(gemini_api)

import os
from google import genai
from google.genai import types

# 1. اتصال به API (کلید از متغیر محیطی GEMINI_API_KEY خوانده می‌شود)
client = genai.Client(api_key= gemini_api)

# 2. تعریف ساختار خروجی مورد نظر (Schema)
# ما به مدل می‌گوییم که دقیقاً چه اطلاعاتی را در چه قالبی می‌خواهیم
nutrition_schema = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "food_items": types.Schema(
            type=types.Type.ARRAY,
            description="A list of all food items mentioned with their calculated nutritional data.",
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "name": types.Schema(type=types.Type.STRING, description="The name of the food (e.g., Apple, Salmon)."),
                    "quantity_g": types.Schema(type=types.Type.NUMBER, description="The weight in grams."),
                    "calories": types.Schema(type=types.Type.NUMBER, description="Estimated total calories."),
                    "protein_g": types.Schema(type=types.Type.NUMBER, description="Estimated protein in grams."),
                },
            ),
        ),
        "exercise_items": types.Schema(
            type=types.Type.ARRAY,
            description="A list of all exercises mentioned with estimated burned calories.",
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "activity": types.Schema(type=types.Type.STRING, description="The type of exercise (e.g., Running, Yoga)."),
                    "duration_min": types.Schema(type=types.Type.NUMBER, description="Duration in minutes."),
                    "calories_burned": types.Schema(type=types.Type.NUMBER, description="Estimated calories burned."),
                },
            ),
        ),
    },
)

# 3. تعریف Prompt با ورودی کاربر
user_input = "I ate 200 grams of chicken and ran 3 miles in 30 minutes."

prompt = (
    "Analyze the following text for both food consumption and exercise performed. "
    "Estimate the nutritional values and calories burned based on general data. "
    f"User input: {user_input}"
)

# 4. فراخوانی API با حالت خروجی JSON
response = client.models.generate_content(
    model='gemini-2.5-flash', # مدل قوی و سریع برای این کار
    contents=prompt,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=nutrition_schema,
    ),
)

# 5. نمایش خروجی
import json
print(json.loads(response.text))