from fastapi import FastAPI, status, Depends, HTTPException
from routers.authentication import auth
from routers.users import users
from routers.venue import venue
from routers.venue import venue_events
from routers.venue import venue_images
from routers.venue import all_data
from routers.venue import test
from database.database import engine, SessionLocal
from typing import Annotated
from sqlalchemy.orm import Session
import models.api_users as models
from models.api_users import ApiUsers as Users
import routers.authentication.auth
from routers.authentication.auth import get_current_user
import logging
logger = logging.getLogger(__name__)
# Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     filename='logs/app.log',
#     filemode='a'
# )

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", status_code=status.HTTP_200_OK)
async def user(user: user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Fail")
    return {'User': user}

@app.get("/users", status_code=201)
async def get_allusers(user: user_dependency, db:db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Authentication Fail")
    
    logger.info(f"User Authenticated: {user}")
    return db.query(Users).all()

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(venue.router)
app.include_router(venue_events.router)
app.include_router(venue_images.router)
app.include_router(all_data.router)
# app.include_router(test)
#app.include_router(todo.router)