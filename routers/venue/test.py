# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from models.venue import test
# from schemas.test import testrequest
# from database.database import SessionLocal, engine


# router = APIRouter()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/test/", status_code=201)
# async def test(item: testrequest, db: Session = Depends(get_db)):
#     db_item = test(sub_category_id=item.sub_category_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item