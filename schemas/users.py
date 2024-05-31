from pydantic import BaseModel

class UsersRequest(BaseModel):
    name: str
    user_type: str
    email:str
    password:str
    #impliment all required columns