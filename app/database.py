from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

# connect to the database using the URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# this is used to talk to SQL database using session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# To create table and stuff
Base = declarative_base()


# A function to handle every incoming request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
