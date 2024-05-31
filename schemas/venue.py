from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional


class VenueBase(BaseModel):
    lang: str = 'en'
    sub_category_id: int
    status: int = 0
    assign_featured: int = 0
    reservation: int = 0
    slug: str
    venue_capacity: Optional[int] = None
    lat: Optional[str] = None
    long: Optional[str] = None
    location: Optional[str] = None
    country: Optional[str] = None
    city: Optional[str] = None
    area: Optional[str] = None
    start_date_time: Optional[datetime] = None
    end_date_time: Optional[datetime] = None
    cusine_name: Optional[str] = None
    view_floor_plan: Optional[str] = None
    city_id: int = 0
    images: Optional[str] = None
    feature_image: Optional[str] = None
    icon: Optional[str] = None
    video: Optional[str] = None
    amenity_id: Optional[str] = None
    landmark_id: Optional[str] = None
    whatsapp: Optional[str] = None
    contact: Optional[str] = None
    email: Optional[str] = None
    start_time: Optional[time] = None
    end_time: Optional[time] = None
    dynamic_main_ids: Optional[str] = None
    dynamic_sub_ids: Optional[str] = None
    prices: Optional[str] = None
    view_menu: Optional[str] = None
    youtube_img: Optional[int] = None
    map_review: Optional[int] = None
    map_rating: Optional[float] = None
    created_by: int = 1
    is_publisher: int = 0
    meta_img_alt: Optional[str] = None
    meta_img_title: Optional[str] = None
    meta_img_description: Optional[str] = None
    stories: Optional[str] = None
    is_popular: int = 0
    is_hot: int = 0
    is_trending: int = 0
    is_verified: Optional[int] = None
    opening_hours: Optional[str] = None
    discount_offer: float = 0
    keywords: str = '[]'
    deleted_at: Optional[datetime] = None
    title: str
    views: int = 0
    description: str
    is_draft: int = 0
    meta_title: Optional[str] = None
    meta_description: Optional[str] = None
    meta_tags: Optional[str] = None
    status_text: Optional[str] = None

    class Config:
        orm_mode = True


class VenueCreate(VenueBase):
    pass


class VenueUpdate(VenueBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
