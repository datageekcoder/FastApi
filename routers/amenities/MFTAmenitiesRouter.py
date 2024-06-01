from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from starlette import status
from database.database import get_db
from models.amenities.mft_amenities import MFTAmenities
from routers.authentication.auth import get_current_user
from schemas.amenities.MFTAmenitiesSchema import MFTAmenitiesResponse, MFTAmenitiesRequest
from schemas.users import UserResponse

router = APIRouter(tags=['MFT Amenities'])


@router.get("/amenities/{amenities_id}", response_model=MFTAmenitiesResponse)
async def get_amenities(
        amenities_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTAmenities).filter(MFTAmenities.id == amenities_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "Amenities not found."
            }
            return JSONResponse(status_code=404, content=content)

        data = MFTAmenitiesResponse.from_orm(db_obj).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "Amenities retrieved successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to retrieve amenities."
        }
        return JSONResponse(status_code=400, content=content)


@router.post("/amenities", response_model=MFTAmenitiesResponse)
async def create_amenities(amenities: MFTAmenitiesRequest, db: Session = Depends(get_db),
                           current_user: UserResponse = Depends(get_current_user)):
    try:
        amenities = amenities.dict()
        db_amenities = MFTAmenities(**amenities)
        db.add(db_amenities)
        db.commit()
        db.refresh(db_amenities)
        data = MFTAmenitiesResponse.from_orm(db_amenities).dict()
        data = jsonable_encoder(data)
        content = {
            "status": "SUCCESS",
            "data": data,
            "message": "Amenities created successfully!"
        }
        return JSONResponse(status_code=201, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Amenities creation failed."
        }
        return JSONResponse(status_code=400, content=content)


@router.put("/amenities/{amenities_id}", response_model=MFTAmenitiesResponse)
async def update_amenities(amenities_id: int, amenities: MFTAmenitiesRequest, db: Session = Depends(get_db),
                           current_user: UserResponse = Depends(get_current_user)):
    db_amenities = db.query(MFTAmenities).filter(MFTAmenities.id == amenities_id).first()
    if db_amenities is None:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"status": "ERROR", "data": {}, "message": "Amenities not found"}
        )
    amenities = amenities.dict(exclude_unset=True)
    for var, value in amenities.items():
        if value is not None:
            setattr(db_amenities, var, value)
    db.commit()
    db.refresh(db_amenities)
    data = MFTAmenitiesResponse.from_orm(db_amenities).dict()
    data = jsonable_encoder(data)
    content = {
        "status": "SUCCESS",
        "data": data,
        "message": "Amenities updated successfully!"
    }
    return JSONResponse(content=content, status_code=status.HTTP_200_OK)


@router.delete("/amenities/{amenities_id}")
async def delete_amenities(
        amenities_id: int,
        db: Session = Depends(get_db),
        current_user: UserResponse = Depends(get_current_user)
):
    try:
        db_obj = db.query(MFTAmenities).filter(MFTAmenities.id == amenities_id).first()
        if db_obj is None:
            content = {
                "status": "FAIL",
                "data": {},
                "message": "Amenities not found or already deleted"
            }
            return JSONResponse(status_code=404, content=content)

        db.delete(db_obj)
        db.commit()

        content = {
            "status": "SUCCESS",
            "data": {},
            "message": "Amenities deleted successfully!"
        }
        return JSONResponse(status_code=200, content=content)
    except Exception as e:
        print(f"Exception: {e}")
        content = {
            "status": "FAIL",
            "data": {},
            "message": "Failed to delete amenities."
        }
        return JSONResponse(status_code=400, content=content)
