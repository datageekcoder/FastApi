from pydantic import BaseModel


class UsersRequest(BaseModel):
    name: str
    user_type: str
    email: str
    password: str
    # implement all required columns
