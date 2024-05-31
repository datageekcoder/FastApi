from database.database import Base
from sqlalchemy import Column, BigInteger, Text, TIMESTAMP
from sqlalchemy.sql import func


class Venue_Reservations(Base):
    __tablename__ = 'mft_venue_reservations'

    id = Column(BigInteger, primary_key=True, index=True)
    user_id = Column(BigInteger, default=0, nullable=False)
    booking_date = Column(TIMESTAMP(timezone=True))
    person = Column(BigInteger, default=0, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
    name = Column(Text)
    mobile_no = Column(Text)
    man = Column(BigInteger)
    woman = Column(Text)
    children = Column(Text)
    venue_id = Column(BigInteger, nullable=False)
    booking_type = Column(BigInteger, nullable=False)
    email = Column(Text)
    message = Column(Text)
