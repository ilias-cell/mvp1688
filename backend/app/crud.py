from sqlalchemy.orm import Session
from . import models, schemas

def get_suppliers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Supplier).offset(skip).limit(limit).all()

def get_supplier(db: Session, supplier_id: int):
    return db.query(models.Supplier).filter(models.Supplier.id == supplier_id).first()

def create_supplier(db: Session, supplier: schemas.SupplierCreate):
    db_obj = models.Supplier(**supplier.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_products(db: Session, skip: int = 0, limit: int = 100, q: str = None):
    query = db.query(models.Product)
    if q:
        query = query.filter(models.Product.name.ilike(f"%{q}%"))
    return query.offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_obj = models.Product(**product.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj