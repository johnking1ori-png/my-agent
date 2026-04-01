from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import requests
from dotenv import load_dotenv
import os

load_dotenv()


app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class Message(BaseModel):
    message: str



@app.post("/chats")
def chats(message: Message):
    
   api_key = os.getenv("API_KEY")
   user_message = message.message
   API_URL = "https://router.huggingface.co/v1/chat/completions"
   
   headers = {
       'Authorization': f"Bearer {api_key}",
       'Content-Type': "application/json"
   }
   body = {
       'model': "meta-llama/Llama-3.1-8B-Instruct",
       "messages": [
        {"role": "user", "content": user_message}
    ]
   }
   
   try:
       
        response = requests.post(
            API_URL, 
            headers=headers, 
            json=body,
            timeout=30
            )
        response.raise_for_status()
   
        data = response.json()
   
        return {"message": data['choices'][0]['message']['content']}
    

   except requests.exceptions.HTTPError as e:
        return {"message": f"HTTP Error: {e}"}
   except Exception as e:
        return {"message": f"Other Error: {e}"}