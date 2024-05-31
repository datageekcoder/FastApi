from pydantic import BaseModel

class testrequest(BaseModel):
    sub_category_id: str

    class Config:
        from_attributes = True