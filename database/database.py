from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
# from sqlalchemy.ext.declarative import declarative_base
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/myfirst"#'sqlite:///./myfinder.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
