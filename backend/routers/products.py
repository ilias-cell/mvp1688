from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/products", tags=["Products"])

class Product(BaseModel):
    id: int
    name: str
    price: float
    supplier: str
    description: str

fake_products = [
    {"id": 1, "name": "Футболка хлопковая", "price": 450, "supplier": "ООО ТекстильПром", "description": "100% хлопок"},
    {"id": 2, "name": "Джинсы мужские", "price": 1200, "supplier": "Стиль+Пошив", "description": "Плотный деним"},
]

@router.get("/")
def get_products():
    return fake_products