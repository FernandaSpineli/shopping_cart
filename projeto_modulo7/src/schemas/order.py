import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field

from src.schemas.address import Address
from src.schemas.product import ProductSchema
from src.schemas.user import UserSchema
from typing import List


class OrderSchema(BaseModel):
    user: UserSchema
    products: List[ProductSchema] = []
    price: Decimal = Field(max_digits=10, decimal_places=2)
    paid: bool = Field(default=False)
    create: datetime.datetime = Field(default=datetime.datetime.now())
    address: Address
    authority: Optional[str] = Field(max_length=100)
