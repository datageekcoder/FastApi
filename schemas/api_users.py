from pydantic import BaseModel


class ApiUsersRequest(BaseModel):
    name: str
    user_type: str
    email: str
    password: str
    # implement all required columns


class ApiUserResponse(ApiUsersRequest):
    id: int

    # Required for ORM based response data to enable ORM mode
    class Config:
        from_attributes = True
