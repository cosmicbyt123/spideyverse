from google import genai
from google.genai import types
from PIL import Image


# Pass your API key explicitly as a string
api_key = "AIzaSyB9pF3je4dUwnyyQcbgC_krTRhU6uVlco0"
client = genai.Client(api_key=api_key)
image = Image.open("D:\START_UP_CODE\GEMINI_API_CODE\download.jpg")


def response(ques):

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[image,ques],
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
    ),
)

    print(response.text)
    
    
