import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

import PIL

# ask Gemini Vision to count the objects from an image and provide the response in the json format
image = PIL.Image.open('assets/objects.jpg')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Generate a json of ingredients with their count present in the image",image])
print(response.text)