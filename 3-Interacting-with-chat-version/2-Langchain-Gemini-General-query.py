import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


# model = genai.GenerativeModel('gemini-pro')
# chat_model = genai.GenerativeModel('gemini-pro')

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")
# General query
response = llm.invoke("Explain Quantum Computing in 100 words?")
print(response.content)