from pydantic import BaseModel

class MenuCreate(BaseModel):
    name: str
    price: float

class MenuResponse(MenuCreate):
    id: int
    is_available: bool

    class Config:
        from_attributes = True
