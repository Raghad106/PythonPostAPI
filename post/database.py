from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()  # must be called before reading the variable
DATABASE_URL = os.getenv("DATABASE_URL")
print("DB URL:", DATABASE_URL)  # for debug

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
