from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.venue.venue_images import Venue_Images
from schemas.venue_images import VenueImageBase, Image
from database.database import get_db
from passlib.context import CryptContext
from typing import Annotated

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]


@router.post("/create_venue_images/", status_code=201)
async def create_venue_images(item: VenueImageBase, db: Session = Depends(get_db)):
    db_item = Venue_Images(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@router.get("/get_venue_images/{item_id}", status_code=200)
def read_venue_images(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Venue_Images).filter(Venue_Images.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put("/update_venue_images/{item_id}", status_code=200)
def update_venue_images(item_id: int, item: Image, db: Session = Depends(get_db)):
    db_item = db.query(Venue_Images).filter(Venue_Images.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)
    return db_item
