import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])


from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro")

# Multiple inputs
batch_responses = llm.batch(
    [
        "Who is the Prime Minister of Cabo Verde?",
        "What is the capital of Cabo Verde?",
        "Who is the Prime Minister of São Tomé e Príncipe?",
        "What is the capital of São Tomé e Príncipe?",
    ]
)
for response in batch_responses:
    print(response.content)
