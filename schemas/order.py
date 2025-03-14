from pydantic import BaseModel
from typing import Optional

class OrderCreate(BaseModel):
    order_id: int
    user_id: int
    distance_km: float
    weather: str
    traffic_level: str
    time_of_day: str
    vehicle_type: str
    preparation_time_min: int
    courier_experience_yrs: float
    delivery_time_min: int

class OrderResponse(OrderCreate):
    id: int

    class Config:
        orm_mode = True