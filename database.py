from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file
DATABASE_URL = "sqlite:///./addresses.db"

# Create database engine (connection)
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # allow multi-thread access (required for FastAPI)
)

# Create session factory (used to interact with DB)
SessionLocal = sessionmaker(
    autocommit=False,   # require explicit commit()
    autoflush=False,    # prevent automatic flush before queries
    bind=engine         # bind session to this database
)

# Base class for all models (tables)
Base = declarative_base()