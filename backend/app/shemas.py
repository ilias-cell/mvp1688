from pydantic import BaseModel
from typing import Optional

class SupplierBase(BaseModel):
    name: str
    description: Optional[str] = None
    contact_email: Optional[str] = None

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    moq: Optional[int] = 1
    image: Optional[str] = None

class ProductCreate(ProductBase):
    supplier_id: int

class Product(ProductBase):
    id: int
    supplier: Supplier
    class Config:
        orm_mode = True