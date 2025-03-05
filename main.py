import pytesseract
from dotenv import load_dotenv
import os

from PIL import Image
from openai import OpenAI

load_dotenv()

lines = pytesseract.image_to_string('report.jpg', lang='rus')

OPEN_API_KEY = os.getenv('OPEN_API_KEY')
client = OpenAI(api_key=OPEN_API_KEY)


completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)
