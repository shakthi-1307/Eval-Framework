import os 
from groq import Groq 
from dotenv import load_dotenv

load_dotenv()

class GroqLLM:
    
    def __init__(self):
        self.client  = Groq(
            api_key = os.getenv("GROQ_API_KEY")
        )
        
        self.model = os.getenv("GROQ_MODEL")
        
        if not self.model:
            raise ValueError("Groq Model is not configured.")
        
    def generate(self,prompt: str) -> str:
        
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [
                {
                    "role":"user",
                    "content":prompt
                }
            ],
            temperature = 0
        )
        
        return response.choices[0].message.content or ""