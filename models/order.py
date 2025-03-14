from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, unique=True, index=True)
    distance_km = Column(Float)
    weather = Column(String)
    traffic_level = Column(String)
    time_of_day = Column(String)
    vehicle_type = Column(String)
    preparation_time_min = Column(Integer)
    courier_experience_yrs = Column(Float)
    delivery_time_min = Column(Integer)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="orders")