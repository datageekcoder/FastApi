from database.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
 

class test(Base):
    __tablename__ = 'test'

    id = Column(Integer, primary_key=True, index=True)
    sub_category_id = Column(String)