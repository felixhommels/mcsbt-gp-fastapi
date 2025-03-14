from pydantic import BaseModel
from typing import List

class OrderBase(BaseModel):
    order_id: int

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    orders: List[OrderBase] = []

    class Config:
        orm_mode = True

class UserCreateResponse(UserBase):
    id: int
    api_token: str

    class Config:
        orm_mode = True