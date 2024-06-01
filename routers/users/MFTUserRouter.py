import os
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, Form, UploadFile, File, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from schemas.user.MFTUsersSchema import MFTUserResponse
from sqlalchemy.orm import Session
from database.database import get_db
from models.users import MFTUsers
from routers.authentication.auth import get_current_user
from schemas.users import UserResponse

router = APIRouter(tags=['MFT User'])

UPLOAD_DIRECTORY = "./uploads/users"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@router.get("/users/{user_id}", response_model=MFTUserResponse)
async def get_users(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTUsers).filter(MFTUsers.id == user_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "User not found."
            }
            return JSONResponse(status_code=404, content=content)

        data = MFTUserResponse.from_orm(db_obj).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "User retrieved successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to retrieve user."
        }
        return JSONResponse(status_code=400, content=content)


@router.post("/users", response_model=MFTUserResponse)
async def create_user(
        name: str = Form(...),
        user_type: int = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        username: str = Form(...),
        mobile_no: str = Form(...),
        profile_image: UploadFile = File(None),
        qr_image: Optional[str] = Form(None),
        company_name: Optional[str] = Form(None),
        address: Optional[str] = Form(None),
        business_type: Optional[str] = Form(None),
        publisher_category_type: Optional[int] = Form(0),
        list_category: Optional[str] = Form(None),
        list_subcategory: Optional[str] = Form(None),
        status_text: Optional[str] = Form(None),
        location: Optional[str] = Form(None),
        ip_location: Optional[str] = Form(None),
        lat: Optional[str] = Form(None),
        lng: Optional[str] = Form(None),
        gender: Optional[str] = Form(None),
        dob: Optional[datetime] = Form(None),
        city: Optional[str] = Form(None),
        town: Optional[str] = Form(None),
        status: Optional[int] = Form(1),
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        user_data = {
            "name": name,
            "user_type": user_type,
            "email": email,
            "password": password,
            "username": username,
            "mobile_no": mobile_no,
            "qr_image": qr_image,
            "company_name": company_name,
            "address": address,
            "business_type": business_type,
            "publisher_category_type": publisher_category_type,
            "list_category": list_category,
            "list_subcategory": list_subcategory,
            "status_text": status_text,
            "location": location,
            "ip_location": ip_location,
            "lat": lat,
            "lng": lng,
            "gender": gender,
            "dob": dob,
            "city": city,
            "town": town,
            "status": status,
            "created_by": current_user.get('id', None)
        }

        # Save the profile image if provided
        if profile_image:
            file_path = os.path.join(UPLOAD_DIRECTORY, profile_image.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await profile_image.read())
            user_data["profile_picture"] = file_path.replace('./', '/')

        db_user = MFTUsers(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        data = MFTUserResponse.from_orm(db_user).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "User is created successfully!"
        }
        return JSONResponse(status_code=201, content=content)

    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "SUCCESS",
            "data": {},
            "message": "User creation failed!"
        }
        return JSONResponse(status_code=400, content=content)


@router.put("/users/{user_id}", response_model=MFTUserResponse)
async def update_user(
        user_id: int,
        name: Optional[str] = Form(None),
        user_type: Optional[int] = Form(None),
        email: Optional[str] = Form(None),
        password: Optional[str] = Form(None),
        username: Optional[str] = Form(None),
        mobile_no: Optional[str] = Form(None),
        profile_image: UploadFile = File(None),
        qr_image: Optional[str] = Form(None),
        company_name: Optional[str] = Form(None),
        address: Optional[str] = Form(None),
        business_type: Optional[str] = Form(None),
        publisher_category_type: Optional[int] = Form(0),
        list_category: Optional[str] = Form(None),
        list_subcategory: Optional[str] = Form(None),
        status_text: Optional[str] = Form(None),
        location: Optional[str] = Form(None),
        ip_location: Optional[str] = Form(None),
        lat: Optional[str] = Form(None),
        lng: Optional[str] = Form(None),
        gender: Optional[str] = Form(None),
        dob: Optional[datetime] = Form(None),
        city: Optional[str] = Form(None),
        town: Optional[str] = Form(None),
        status: Optional[int] = Form(1),
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_user = db.query(MFTUsers).filter(MFTUsers.id == user_id).first()
        if not db_user:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "User not found"
            }
            return JSONResponse(status_code=404, content=content)

        user_data = {
            "name": name,
            "user_type": user_type,
            "email": email,
            "password": password,
            "username": username,
            "mobile_no": mobile_no,
            "qr_image": qr_image,
            "company_name": company_name,
            "address": address,
            "business_type": business_type,
            "publisher_category_type": publisher_category_type,
            "list_category": list_category,
            "list_subcategory": list_subcategory,
            "status_text": status_text,
            "location": location,
            "ip_location": ip_location,
            "lat": lat,
            "lng": lng,
            "gender": gender,
            "dob": dob,
            "city": city,
            "town": town,
            "status": status
        }

        # Save the profile image if provided
        if profile_image:
            file_path = os.path.join(UPLOAD_DIRECTORY, profile_image.filename)
            with open(file_path, "wb") as buffer:
                buffer.write(await profile_image.read())
            user_data["profile_picture"] = file_path.replace('./', '/')

        # Update fields in the database object
        for key, value in user_data.items():
            if value is not None:
                setattr(db_user, key, value)

        db.commit()
        db.refresh(db_user)

        data = MFTUserResponse.from_orm(db_user).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "User is updated successfully!"
        }
        return JSONResponse(status_code=200, content=content)

    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "User update failed"
        }
        return JSONResponse(status_code=400, content=content)


@router.delete("/users/{user_id}")
async def delete_users(
        user_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTUsers).filter(MFTUsers.id == user_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "User not found or already deleted"
            }
            return JSONResponse(status_code=404, content=content)

        db.delete(db_obj)
        db.commit()

        content = {
            "status": "SUCCESS",
            "data": {},
            "message": "User deleted successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to delete user."
        }
        return JSONResponse(status_code=400, content=content)
