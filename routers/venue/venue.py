from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.venue.venue import Venues
from schemas.venue import VenueBase, VenueUpdate
from database.database import get_db
from passlib.context import CryptContext
from typing import Annotated


router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

db_dependency = Annotated[Session, Depends(get_db)]

@router.post("/create_venue/", status_code=201)
async def create_venue(item: VenueBase, db: Session = Depends(get_db)):
    db_item = Venues(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/get_venue/{item_id}", status_code=200)
def read_venue(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Venues).filter(Venues.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@router.put("/update_venue/{item_id}", status_code=200)
def update_venue(item_id: int, item: VenueUpdate, db: Session = Depends(get_db)):
    db_item = db.query(Venues).filter(Venues.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for key, value in item.dict(exclude_unset=True).items():
        setattr(db_item, key, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item
