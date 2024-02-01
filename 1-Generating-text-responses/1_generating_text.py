import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

model = genai.GenerativeModel('gemini-pro')


response = model.generate_content("List 5 planets each with an interesting fact")
print(response.text)

response = model.generate_content("what are top 5 frequently used emojis?")
print(response.text)