from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VenueReservationsBase(BaseModel):
    user_id: int = 0
    booking_date: Optional[datetime] = None
    person: int = 0
    name: Optional[str] = None
    mobile_no: Optional[str] = None
    man: Optional[int] = None
    woman: Optional[str] = None
    children: Optional[str] = None
    venue_id: int
    booking_type: int
    email: Optional[str] = None
    message: Optional[str] = None

    class Config:
        orm_mode = True

class VenueReservationsCreate(VenueReservationsBase):
    pass

class VenueReservations(VenueReservationsBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
