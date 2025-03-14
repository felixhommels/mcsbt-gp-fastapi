from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base
import secrets

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    api_token = Column(String, unique=True, index=True)
    
    orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")

    def generate_api_token(self):
        self.api_token = secrets.token_hex(32)
        return self.api_token
