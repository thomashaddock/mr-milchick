from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any

from app.services.openai_service import OpenAIService

router = APIRouter()

# Create service instance
openai_service = OpenAIService()

class MessageRequest(BaseModel):
    message: str

class MessageResponse(BaseModel):
    response: str
    properties: List[Dict[str, Any]] = []

@router.post("/chat", response_model=MessageResponse)
async def chat(request: MessageRequest):
    try:
        # Get response from OpenAI
        response_text = await openai_service.get_response(request.message)
        
        # For MVP: Return mock properties if message mentions apartments
        properties = []
        if any(keyword in request.message.lower() for keyword in ["apartment", "building", "rent"]):
            properties = [
                {
                    "id": "1",
                    "address": "123 Manhattan Ave",
                    "price": "$3,500/month",
                    "bedrooms": 1,
                    "bathrooms": 1,
                    "sqft": 750,
                    "imageUrl": "https://via.placeholder.com/300x200?text=Apartment"
                },
                {
                    "id": "2",
                    "address": "456 Central Park West",
                    "price": "$5,200/month",
                    "bedrooms": 2,
                    "bathrooms": 2,
                    "sqft": 1100,
                    "imageUrl": "https://via.placeholder.com/300x200?text=Apartment"
                }
            ]
        
        return MessageResponse(response=response_text, properties=properties)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))