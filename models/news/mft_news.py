from sqlalchemy import Column, BigInteger, String, Text, SmallInteger, TIMESTAMP
from datetime import datetime
from database.database import Base


class MFTNews(Base):
    __tablename__ = "mft_news"

    id = Column(BigInteger, primary_key=True, index=True)
    major_category_id = Column(BigInteger, nullable=False)
    main_category_id = Column(BigInteger, nullable=False)
    sub_category_id = Column(BigInteger, nullable=False)
    slug = Column(String(191), nullable=False)
    publish_date = Column(TIMESTAMP(timezone=True), nullable=True)
    publisher = Column(Text, nullable=True)
    feature_image = Column(Text, nullable=True)
    alt_texts_en = Column(String(191), nullable=True)
    alt_texts_ar = Column(String(191), nullable=True)
    alt_texts_zh = Column(String(191), nullable=True)
    is_publisher = Column(BigInteger, default=0, nullable=False)
    is_featured = Column(SmallInteger, default=0, nullable=False)
    is_hot = Column(SmallInteger, default=0, nullable=False)
    is_trending = Column(SmallInteger, default=0, nullable=False)
    is_popular = Column(SmallInteger, default=0, nullable=False)
    is_draft = Column(SmallInteger, default=0, nullable=False)
    status = Column(SmallInteger, default=0, nullable=False)
    created_by = Column(BigInteger, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow)
    updated_at = Column(TIMESTAMP(timezone=True), default=datetime.utcnow, onupdate=datetime.utcnow)
