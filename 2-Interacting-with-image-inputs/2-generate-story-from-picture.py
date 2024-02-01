import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

import PIL

# ask Gemini LLM to generate a story from the given image.
image = PIL.Image.open('assets/messi.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Write a story from the picture",image])
print(response.text)