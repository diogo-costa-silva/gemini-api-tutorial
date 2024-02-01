import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


model = genai.GenerativeModel('gemini-pro')

chat_model = genai.GenerativeModel('gemini-pro')
chat = chat_model .start_chat(history=[])

response = chat.send_message("Which is one of the best place to visit in Portugal during summer?")
print(response.text)
response = chat.send_message("Tell me more about that place in 65 words please")
print(response.text)
print(chat.history)