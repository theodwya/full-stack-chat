# app/schemas.py
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    Pydantic model for validating user creation input.
    - username: Required string value
    - email: Must be a valid email address
    - password: Required string value
    """
    username: str
    email: EmailStr
    password: str
