from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    contact_email = Column(String, nullable=True)
    products = relationship("Product", back_populates="supplier")

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, default=0.0)
    moq = Column(Integer, default=1)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    image = Column(String, nullable=True)
    supplier = relationship("Supplier", back_populates="products")