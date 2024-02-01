import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Find the differences between the given images",
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/237/200/300"
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/219/5000/3333"
        }
    ]
)

response = llm.invoke([message])
print(response.content)