from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models.user import User
from models.order import Order
from schemas.user import UserCreate, UserResponse, UserCreateResponse
from schemas.order import OrderCreate, OrderResponse
from typing import List
import uvicorn
from fastapi import Header

app = FastAPI()

def get_current_user(api_token: str = Header(None), db: Session = Depends(get_db)):
    if not api_token:
        raise HTTPException(status_code=401, detail="Missing API Token")

    user = db.query(User).filter(User.api_token == api_token).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid API Token")

    return user

@app.post("/create_user", response_model=UserCreateResponse)
def create_user(user: UserCreate, database: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db_user.generate_api_token()
    database.add(db_user)
    database.commit()
    database.refresh(db_user)
    return db_user

@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, database: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/create_order", response_model=OrderResponse)
def create_order(order: OrderCreate, database: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user = database.query(User).filter(User.id == order.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_order = Order(
        order_id=order.order_id,
        user_id=order.user_id, 
        distance_km=order.distance_km,
        weather=order.weather,
        traffic_level=order.traffic_level,
        time_of_day=order.time_of_day,
        vehicle_type=order.vehicle_type,
        preparation_time_min=order.preparation_time_min,
        courier_experience_yrs=order.courier_experience_yrs,
        delivery_time_min=order.delivery_time_min
    )

    database.add(db_order)
    database.commit()
    database.refresh(db_order)

    return db_order

@app.get("/user/{user_id}/orders", response_model=List[OrderResponse])
def get_user_orders(user_id: int, database: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    orders = database.query(Order).filter(Order.user_id == user_id).all()
    if not orders:
        raise HTTPException(status_code=404, detail="No orders found for this user")
    return orders

@app.get("/order/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, database: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    order = database.query(Order).filter(Order.order_id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)