from datetime import datetime
from typing import Optional
from pydantic import BaseModel


# Base schema
class MFTNewsDetailsBase(BaseModel):
    news_id: int
    lang: Optional[str] = 'en'
    title: str
    description: str
    status_text: Optional[str] = None
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_tags: Optional[str] = None
    is_draft: bool = False
    views: Optional[int] = 0


# Schema for creating a new entry
class MFTNewsDetailsCreate(MFTNewsDetailsBase):
    pass


# Schema for updating an existing entry
class MFTNewsDetailsUpdate(BaseModel):
    news_id: Optional[int] = None
    lang: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    status_text: Optional[str] = None
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_tags: Optional[str] = None
    is_draft: Optional[bool] = None
    views: Optional[int] = None


# Schema for response
class MFTNewsDetailsResponse(MFTNewsDetailsBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
