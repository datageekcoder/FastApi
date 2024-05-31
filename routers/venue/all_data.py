from fastapi import APIRouter, Depends, HTTPException
from passlib.context import CryptContext
from database.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import DeclarativeMeta
from models.venue.venue import Venues
from models.venue.venue_images import Venue_Images
from models.venue.venue_events import Venue_Events
import json

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def to_dict(obj):
    if isinstance(obj.__class__, DeclarativeMeta):
        # an SQLAlchemy model
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
            data = obj.__getattribute__(field)
            try:
                json.dumps(data)  # this will raise an exception if the value is not serializable
                fields[field] = data
            except TypeError:
                fields[field] = None
        return fields
    return None


@router.get("/get_all_data/{venue_id}")
def get_all_data(venue_id: int, db: Session = Depends(get_db)):
    venues = db.query(Venues).all()
    venue_images = db.query(Venue_Images).all()
    venue_events = db.query(Venue_Events).all()

    response_data = {
        "venues": [to_dict(venue) for venue in venues],
        "venue_images": [to_dict(img) for img in venue_images],
        "venue_events": [to_dict(evt) for evt in venue_events]
    }

    return response_data

    # return {
    #     "venues": [
    #         {
    #             "id": venue.id,
    #             "location": venue.location,

    #         } for venue in venues
    #     ],
    #     "venue_images": [
    #         {"id": img.id, "venue_id": img.venue_id}
    #         for img in venue_images
    #     ],
    #     "venue_events": [
    #         {"id": evt.id, "venue_id": evt.venue_id}
    #         for evt in venue_events
    #     ]
    # }
