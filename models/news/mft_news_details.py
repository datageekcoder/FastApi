from sqlalchemy import Column, BigInteger, String, Text, TIMESTAMP, Boolean, ForeignKey
from datetime import datetime
from database.database import Base


class MFTNewsDetails(Base):
    __tablename__ = "mft_news_details"

    id = Column(BigInteger, primary_key=True, index=True)
    news_id = Column(BigInteger, ForeignKey('mft_news.id'), nullable=False)
    lang = Column(String(5), nullable=False, default='en')
    title = Column(String(191), nullable=False)
    description = Column(Text, nullable=False)
    status_text = Column(Text, nullable=True)
    meta_title = Column(Text, nullable=True)
    meta_description = Column(Text, nullable=True)
    meta_tags = Column(Text, nullable=True)
    is_draft = Column(Boolean, default=False, nullable=False)
    views = Column(BigInteger, default=0, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    updated_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
