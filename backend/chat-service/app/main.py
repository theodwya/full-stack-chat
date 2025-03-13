from fastapi import FastAPI
from app.database import Base, engine
from app.routes import chat_routes

# Initialize all database tables upon service start
Base.metadata.create_all(bind=engine)

# Create the FastAPI application
app = FastAPI()

# Facade Pattern:
# The FastAPI instance acts as a simplified interface for interacting with
# the underlying user service (routes, models, database).
app.include_router(chat_routes.router, prefix="/api/v1/chat", tags=["Chat"])
