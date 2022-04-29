from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class ProductBase(BaseModel):
    low_price: Decimal
    high_price: Decimal
    demand_qty: int
    offers_qty: int
    bought_qty: int
    sold_qty: int
    time_created: datetime


class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True


class ProductDebugV1(BaseModel):
    low_price: Decimal
    high_price: Decimal

    class Config:
        orm_mode = True
