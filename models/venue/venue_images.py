from database.database import Base
from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.sql import func

class Venue_Images(Base):
    __tablename__ = 'mft_venue_images'

    id = Column(Integer, primary_key=True, nullable=False)
    venue_id = Column(BigInteger, ForeignKey("mft_venues.id"))
    image_type = Column(String(191), nullable=False)
    image = Column(String(191), nullable=False)
    alt_title = Column(Text)
    alt_texts = Column(String(191))
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), onupdate=func.now())
