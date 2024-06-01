from datetime import datetime
from typing import Optional
from pydantic import Field, BaseModel


class MFTUserBase(BaseModel):
    name: str
    user_type: int
    email: str
    username: str
    mobile_no: str
    profile_picture: Optional[str] = None
    qr_image: Optional[str] = None
    company_name: Optional[str] = None
    address: Optional[str] = None
    business_type: Optional[str] = None
    publisher_category_type: Optional[int] = Field(default=0)
    list_category: Optional[str] = None
    list_subcategory: Optional[str] = None
    status_text: Optional[str] = None
    location: Optional[str] = None
    ip_location: Optional[str] = None
    lat: Optional[str] = None
    lng: Optional[str] = None
    gender: Optional[str] = None
    dob: Optional[datetime] = None
    city: Optional[str] = None
    town: Optional[str] = None
    status: Optional[int] = Field(default=1)


class MFTUserResponse(MFTUserBase):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
