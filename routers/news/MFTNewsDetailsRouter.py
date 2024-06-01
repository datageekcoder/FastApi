from datetime import datetime
from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from starlette import status
from database.database import get_db
from models.news.mft_news_details import MFTNewsDetails
from routers.authentication.auth import get_current_user
from schemas.news.MFTNewsDetailsSchema import MFTNewsDetailsResponse, MFTNewsDetailsUpdate, MFTNewsDetailsCreate
from schemas.users import UserResponse

router = APIRouter(tags=['MFT News Details'])


@router.get("/news-details/{news_details_id}", response_model=MFTNewsDetailsResponse)
async def get_mft_news_details(
        news_detail_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTNewsDetails).filter(MFTNewsDetails.id == news_detail_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "News details not found."
            }
            return JSONResponse(status_code=404, content=content)

        data = MFTNewsDetailsResponse.from_orm(db_obj).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "News details retrieved successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to retrieve news details."
        }
        return JSONResponse(status_code=400, content=content)


@router.post("/news-details", response_model=MFTNewsDetailsResponse)
async def create_news_details(news_details: MFTNewsDetailsCreate, db: Session = Depends(get_db),
                              current_user: UserResponse = Depends(get_current_user)):
    try:
        news_details = news_details.dict()
        db_news_details = MFTNewsDetails(**news_details)
        db.add(db_news_details)
        db.commit()
        db.refresh(db_news_details)
        data = MFTNewsDetailsResponse.from_orm(db_news_details).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "News details created successfully!"
        }
        return JSONResponse(status_code=201, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "News details creation failed."
        }
        return JSONResponse(status_code=400, content=content)


@router.put("/news-details/{news_details_id}", response_model=MFTNewsDetailsResponse)
async def update_news_details(news_details_id: int, news_details: MFTNewsDetailsUpdate, db: Session = Depends(get_db),
                              current_user: UserResponse = Depends(get_current_user)):
    db_news_details = db.query(MFTNewsDetails).filter(MFTNewsDetails.id == news_details_id).first()
    if db_news_details is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"status": "ERROR", "data": {}, "message": "News details not found or already deleted"}
        )
    news_details = news_details.dict(exclude_unset=True)
    for var, value in news_details.items():
        if value is not None:
            setattr(db_news_details, var, value)
    db.commit()
    db.refresh(db_news_details)
    data = MFTNewsDetailsResponse.from_orm(db_news_details).dict()
    data = jsonable_encoder(data)
    content = {
        "status": "SUCCESS",
        "data": data,
        "message": "News details updated successfully!"
    }
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@router.delete("/news-details/{news_details_id}")
async def delete_mft_news_details(
        news_details_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTNewsDetails).filter(MFTNewsDetails.id == news_details_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "News details not found."
            }
            return JSONResponse(status_code=404, content=content)

        db.delete(db_obj)
        db.commit()

        content = {
            "status": "SUCCESS",
            "data": {},
            "message": "News details deleted successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to delete news details."
        }
        return JSONResponse(status_code=400, content=content)
