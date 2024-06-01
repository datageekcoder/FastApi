from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class MFTNewsBase(BaseModel):
    major_category_id: int
    main_category_id: int
    sub_category_id: int
    slug: str
    publish_date: Optional[datetime] = None
    publisher: Optional[str] = None
    feature_image: Optional[str] = None
    alt_texts_en: Optional[str] = None
    alt_texts_ar: Optional[str] = None
    alt_texts_zh: Optional[str] = None
    is_publisher: int = 0
    is_featured: int = 0
    is_hot: int = 0
    is_trending: int = 0
    is_popular: int = 0
    is_draft: int = 0
    status: int = 0
    created_by: int


class MFTNewsResponse(MFTNewsBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
