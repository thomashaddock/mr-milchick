import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.conversation import router as conversation_router

app = FastAPI(
    title="Mr. Milchick API",
    description="Manhattan Real Estate Assistant API",
    version="0.1.0"
)

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversation_router, prefix="/api/conversation", tags=["conversation"])

@app.get("/")
async def root():
    return {"message": "Welcome to Mr. Milchick API"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)