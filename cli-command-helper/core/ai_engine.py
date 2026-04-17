from google import genai
import os
from dotenv import load_dotenv

load_dotenv()  # VERY IMPORTANT

API_KEY = os.getenv("GEMINI_API_KEY") # API KEY

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-2.5-flash"

def ask_ai(user_input):
    prompt = f"""
    Convert this task into a shell command.

    Task: {user_input}

    STRICT FORMAT:
    Explanation:<Short explanation>
    Command:<Single line command>
    """

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text
