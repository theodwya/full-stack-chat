from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database connection parameters
DATABASE_URL = "postgresql://postgres:password@10.0.0.40:5433/userdb"

# Factory Method Pattern: Encapsulates the logic for creating
# a SQLAlchemy engine object.


def create_engine_instance():
    """
    Factory Method:
    Creates and returns a SQLAlchemy engine instance, ensuring
    the database connection logic is encapsulated and reusable.
    """
    return create_engine(DATABASE_URL)


# Create the engine using our factory method
engine = create_engine_instance()

# SQLAlchemy Session and Base declarations
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency Injection Pattern:
# Provides a database session for routes/services.


def get_db():
    """
    Dependency Injection:
    Provides a session object to the calling function in a controlled and
    managed way.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
