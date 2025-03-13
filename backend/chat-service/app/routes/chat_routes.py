from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Message
import json

router = APIRouter()

# Observer Pattern: List of connected WebSocket clients (subscribers)
active_connections = []


async def broadcast_message(message: str):
    """
    Observer Pattern:
    Notify all WebSocket subscribers when a new message is received.
    """
    for connection in active_connections:
        await connection.send_text(message)


@router.websocket("/ws")
async def chat_websocket(websocket: WebSocket, db: Session = Depends(get_db)):
    """
    WebSocket Endpoint:
    Implements real-time communication between users using WebSockets.

    1. Accepts incoming WebSocket connections.
    2. Receives chat messages and saves them to the database.
    3. Broadcasts messages to all active connections using the Observer
       Pattern.
    """
    await websocket.accept()
    active_connections.append(websocket)  # Add to subscribers list
    try:
        while True:
            # Receive message from client
            data = await websocket.receive_text()

            # Parse the incoming message (e.g., JSON payload)
            message_data = json.loads(data)
            new_message = Message(
                sender=message_data["sender"],
                recipient=message_data["recipient"],
                content=message_data["content"]
            )
            db.add(new_message)
            db.commit()

            # Notify all connected clients
            await broadcast_message(data)
    except WebSocketDisconnect:
        active_connections.remove(websocket)  # Remove from subscribers list
