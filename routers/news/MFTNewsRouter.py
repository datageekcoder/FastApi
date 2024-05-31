import os
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Form, UploadFile, File, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from database.database import get_db
from models.mft_news import MFTNews
from routers.authentication.auth import get_current_user
from schemas.MFTNewsSchema import MFTNewsResponse
from schemas.users import UserResponse

router = APIRouter(tags=['MFT News'])

UPLOAD_DIRECTORY = "./uploads/news"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@router.get("/mft_news/{news_id}", response_model=MFTNewsResponse)
async def get_mft_news(
        news_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        news_item = db.query(MFTNews).filter(MFTNews.id == news_id).first()
        if news_item is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "News item not found."
            }
            return JSONResponse(status_code=404, content=content)

        data = MFTNewsResponse.from_orm(news_item).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "News item retrieved successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to retrieve news item."
        }
        return JSONResponse(status_code=400, content=content)


@router.post("/mft_news", response_model=MFTNewsResponse)
async def create_mft_news(
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user),
        major_category_id: int = Form(...),
        main_category_id: int = Form(...),
        sub_category_id: int = Form(...),
        slug: str = Form(...),
        alt_texts_en: Optional[str] = Form(None),
        alt_texts_ar: Optional[str] = Form(None),
        alt_texts_zh: Optional[str] = Form(None),
        feature_image: UploadFile = File(...)
):
    try:
        # Save uploaded files
        feature_image_url = ''
        if feature_image:
            file_path = os.path.join(UPLOAD_DIRECTORY, feature_image.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await feature_image.read())
            feature_image_url = file_path.replace('./', '/')

        db_news = MFTNews(
            major_category_id=major_category_id,
            main_category_id=main_category_id,
            sub_category_id=sub_category_id,
            slug=slug,
            feature_image=feature_image_url,
            alt_texts_en=alt_texts_en,
            alt_texts_ar=alt_texts_ar,
            alt_texts_zh=alt_texts_zh,
            created_by=current_user.get('id', ''),
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        db.add(db_news)
        db.commit()
        db.refresh(db_news)
        data = MFTNewsResponse.from_orm(db_news).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "News is created successfully!"
        }
        return JSONResponse(status_code=201, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "News is not create."
        }
        return JSONResponse(status_code=400, content=content)


@router.put("/mft_news/{news_id}", response_model=MFTNewsResponse)
async def update_mft_news(
        news_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user),
        major_category_id: Optional[int] = Form(None),
        main_category_id: Optional[int] = Form(None),
        sub_category_id: Optional[int] = Form(None),
        slug: Optional[str] = Form(None),
        alt_texts_en: Optional[str] = Form(None),
        alt_texts_ar: Optional[str] = Form(None),
        alt_texts_zh: Optional[str] = Form(None),
        feature_image: UploadFile = File(None)
):
    try:
        db_news = db.query(MFTNews).filter(MFTNews.id == news_id).first()
        if db_news is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "News item not found."
            }
            return JSONResponse(status_code=404, content=content)

        update_data = {
            "major_category_id": major_category_id,
            "main_category_id": main_category_id,
            "sub_category_id": sub_category_id,
            "slug": slug,
            "alt_texts_en": alt_texts_en,
            "alt_texts_ar": alt_texts_ar,
            "alt_texts_zh": alt_texts_zh
        }

        if feature_image:
            file_path = os.path.join(UPLOAD_DIRECTORY, feature_image.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await feature_image.read())
            feature_image_url = file_path.replace('./', '/')
            update_data['feature_image'] = feature_image_url

        for key, value in update_data.items():
            if value is not None:
                setattr(db_news, key, value)

        db_news.updated_at = datetime.utcnow()

        db.commit()
        db.refresh(db_news)

        data = MFTNewsResponse.from_orm(db_news).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "News is updated successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "News is not updated."
        }
        return JSONResponse(status_code=400, content=content)


@router.delete("/mft_news/{news_id}", response_model=MFTNewsResponse)
async def delete_mft_news(
        news_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        news_item = db.query(MFTNews).filter(MFTNews.id == news_id).first()
        if news_item is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "News item not found."
            }
            return JSONResponse(status_code=404, content=content)

        db.delete(news_item)
        db.commit()

        content = {
            "status": "SUCCESS",
            "data": {},
            "message": "News item deleted successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to delete news item."
        }
        return JSONResponse(status_code=400, content=content)
