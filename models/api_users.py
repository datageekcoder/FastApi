from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
 

class ApiUsers(Base):
    __tablename__ = 'api_users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)