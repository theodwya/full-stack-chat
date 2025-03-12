from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    """
    Represents the 'users' database table.
    Fields:
    - id: Primary key.
    - username: Unique username for the user.
    - email: Unique email for the user.
    - password: User's password (should be hashed in production!).
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
