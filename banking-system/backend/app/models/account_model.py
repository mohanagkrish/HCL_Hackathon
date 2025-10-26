from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String, nullable=False)
    initial_deposit = Column(Float, nullable=False)
