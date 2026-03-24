from sqlalchemy import create_engine                            #Connect to database using SQLAlchemy
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./addresses.db"

engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False}) #Allow multiple tasks

SessionLocal = sessionmaker(
        autocommit=False,  #Prevent auto submit
        autoflush=False,   #Auto save
        bind=engine)

Base = declarative_base()