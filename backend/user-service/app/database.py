from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Factory Method Pattern: Encapsulates database connection creation
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


# Create the database engine
engine = create_engine(DATABASE_URL)

# Create a configurable session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declare a base class for all models
Base = declarative_base()

# Dependency Injection Pattern:
# Provides a database session for routes/services.


def get_db():
    """
    Factory Method:
    Provides a new database session object each time it is called.
    This allows the User Service to abstract away the connection logic,
    keeping the code modular and testable.

    Dependency Injection:
    Provides a session object to the calling function in a controlled and
    managed way.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
