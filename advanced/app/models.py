from sqlalchemy import Column, Integer, String

from app.database import Base

class DBOrder(Base):

    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    customer = Column(String)
    item = Column(String)
    quantity = Column(Integer)