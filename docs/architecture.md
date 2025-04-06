# Mr. Milchick Architecture

## Overview

Mr. Milchick is structured as a modern web application with a React frontend and FastAPI backend.

## Frontend Architecture

The frontend is built using:

- React for UI components
- Vite as the build tool
- CSS for styling

Key components:

- ChatInterface: Main conversational UI
- PropertyCard: Display for real estate listings
- API utilities for backend communication

## Backend Architecture

The backend is built using:

- FastAPI for API endpoints
- OpenAI API integration for AI responses
- Simple models for conversation and property data

In a production version, this would be enhanced with:

- Database integration (PostgreSQL)
- Vector database for semantic search (Pinecone)
- Authentication and user management
- Integration with real estate APIs (Zillow, StreetEasy, etc.)

## Data Flow

1. User sends a message through the frontend chat interface
2. Message is sent to the backend API
3. Backend processes the message and sends to OpenAI
4. Backend receives response and formats it for the frontend
5. Frontend displays the response and any property listings
