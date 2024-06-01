from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5432/myfirst"  # 'sqlite:///./myfinder.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# To get db session by this get_db method
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()