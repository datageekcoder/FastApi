from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VenueImageBase(BaseModel):
    venue_id: Optional[int] = None
    image_type: str
    image: str
    alt_title: Optional[str] = None
    alt_texts: Optional[str] = None

    class Config:
        from_attributes = True

class VenueImageCreate(VenueImageBase):
    pass

class Image(VenueImageBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
