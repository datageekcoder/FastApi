from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP
from datetime import datetime
from database.database import Base


class MFTAmenities(Base):
    __tablename__ = "mft_amenities"

    id = Column(BigInteger, primary_key=True, index=True)
    lang = Column(String(191), default='en', nullable=False)
    icon_name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    updated_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
