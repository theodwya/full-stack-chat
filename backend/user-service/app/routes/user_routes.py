from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import User
from app.database import get_db
from app.schemas import UserCreate

# API Router for handling user-related endpoints
router = APIRouter()


@router.post("/users/")
def create_user(
        user: UserCreate, db: Session = Depends(get_db)):
    """
    Create User endpoint:
    - This endpoint receives a JSON body with 'username', 'email', and 'password'.
    - The body is parsed and validated using the Pydantic model.

    Args:
        user (UserCreate): Parsed data for user creation.
        db (Session): Database session object.

    Returns:
        dict: Success message with created user's data.

    Strategy Pattern:
    This route uses a specific strategy for user creation:
    - It validates user input.
    - Checks for conflicts (duplicate username/email).
    - Inserts the user into the database.

    Template Method Pattern (Future Enhancements):
    If extended, this could become a base "user_creation" method
    where validation logic is customized for different user types.
    """
    # Strategy: Validation and conflict checking
    existing_user = db.query(User).filter(
        (User.username == user.username) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(
            status_code=400, detail="Username or email already taken")

    # Strategy: Creating a new user
    db_user = User(username=user.username,
                   email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return {
        "message": "User created successfully",
        "user": {"id": db_user.id, "username": db_user.username},
    }
