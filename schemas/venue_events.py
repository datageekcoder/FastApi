from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VenueEventBase(BaseModel):
    venue_id: int
    name: Optional[str] = None
    datetime: Optional[datetime] = None # type: ignore

    class Config:
        orm_mode = True

class VenueEventCreate(VenueEventBase):
    pass

class VenueEvent(VenueEventBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
