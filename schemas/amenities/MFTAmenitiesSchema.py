from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# Base schema
class MFTAmenitiesBase(BaseModel):
    lang: str
    icon_name: str
    description: str


# Schema for request body
class MFTAmenitiesRequest(MFTAmenitiesBase):
    pass


# Schema for response with all fields
class MFTAmenitiesResponse(MFTAmenitiesBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
