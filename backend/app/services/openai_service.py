import os
from openai import OpenAI
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL

class OpenAIService:
    def __init__(self):
        try:
            # Initialize the OpenAI client with your API key
            self.client = OpenAI(api_key=OPENAI_API_KEY)
        except Exception as e:
            print(f"Error initializing OpenAI client: {e}")
            raise
            
        self.model = OPENAI_MODEL
        self.system_prompt = """
        You are Mr. Milchick, an AI-powered Manhattan real estate assistant. 
        Your role is to help users find and learn about residential properties in Manhattan.
        
        When responding to queries about Manhattan buildings or neighborhoods:
        1. Be concise but informative
        2. Maintain a professional, knowledgeable tone
        3. If asked about specific buildings, mention key details like year built, number of units, and notable amenities
        4. If asked about neighborhoods, include information about the character, transportation options, and popular spots
        5. Provide realistic rental or sales price ranges when relevant
        
        Focus exclusively on Manhattan real estate topics.
        """
    
    async def get_response(self, user_message: str) -> str:
        """
        Get a response from OpenAI.
        """
        try:
            # Print debugging information
            print(f"Sending request to OpenAI with message: {user_message}")
            
            # Make the API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=600
            )
            
            # Extract and return the response text
            response_text = response.choices[0].message.content
            print(f"Received response from OpenAI: {response_text[:100]}...")
            return response_text
            
        except Exception as e:
            # For MVP, return a fallback response
            error_message = str(e)
            print(f"Error calling OpenAI: {error_message}")
            return f"I apologize, but I'm having trouble connecting to my knowledge base. Error: {error_message}"