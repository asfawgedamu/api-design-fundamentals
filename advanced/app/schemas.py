from pydantic import BaseModel, Field

class OrderCreate(BaseModel):

    customer: str = Field(..., min_length=2, max_length=50)
    item: str = Field(..., min_length=2, max_length=50)
    quantity: int = Field(..., gt=0, le=20)

class OrderResponse(OrderCreate):

    id: int

    class Config:
        from_attributes = True