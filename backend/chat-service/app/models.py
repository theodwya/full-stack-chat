from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from .database import Base


class Message(Base):
    """
    Active Record Pattern:
    This class represents the 'messages' table in the database.
    Each instance of this class corresponds to a row in the table.
    It encapsulates both the data and behaviors (CRUD operations)
    related to chat messages.
    """
    __tablename__ = "messages"  # Define the database table name

    # Unique identifier for each message
    id = Column(Integer, primary_key=True, index=True)
    # Username of the sender
    sender = Column(String, nullable=False)
    # Username of the recipient
    recipient = Column(String, nullable=False)
    content = Column(String, nullable=False)               # Message content
    # Auto-generated timestamp
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
