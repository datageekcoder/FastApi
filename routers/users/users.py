from datetime import timedelta, datetime
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from database.database import get_db
from models.users import MFTUsers
from schemas.users import UsersRequest
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter()
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


db_dependency = Annotated[Session, Depends(get_db)]


@router.get("/webuser", status_code=200)
async def get_user(db: db_dependency):
    return db.query(MFTUsers).all()


@router.post("/create_webuser", status_code=201)
async def create_user(db: db_dependency, ceate_user_request: UsersRequest):
    create_user_model = MFTUsers(name=ceate_user_request.name,
                                 user_type=ceate_user_request.user_type,
                                 email=ceate_user_request.email,
                                 password=bcrypt_context.hash(ceate_user_request.password)
                                 )

    db.add(create_user_model)
    db.commit()


@router.get("/login_user", status_code=200)
def authenticate_user(username: str, password: str, db: db_dependency):
    user = db.query(MFTUsers).filter(MFTUsers.name == username).first()
    if not user:
        return HTTPException(400, "User not exists")
    if not bcrypt_context.verify(password, user.password):
        return HTTPException(400, "User not authenticated")

    return user
