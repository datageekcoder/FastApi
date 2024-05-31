from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
 

class webUsers(Base):
    __tablename__ = 'mft_users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    user_type = Column(String, unique=True)
    email = Column(String)
    password = Column(String)