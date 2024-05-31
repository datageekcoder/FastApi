from database.database import Base
from sqlalchemy import Column, BigInteger, Text, TIMESTAMP, ForeignKey
from sqlalchemy.sql import func


class Venue_Events(Base):
    __tablename__ = 'mft_venue_events'

    id = Column(BigInteger, primary_key=True, index=True)
    venue_id = Column(BigInteger, ForeignKey("mft_venues.id"))
    name = Column(Text)
    datetime = Column(TIMESTAMP(timezone=True))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
