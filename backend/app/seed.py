from .database import engine, Base, SessionLocal
from ..models import Supplier, Product

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    if db.query(Supplier).count() > 0:
        db.close()
        return
    s1 = Supplier(name="ООО ТекстильПром", description="Производитель трикотажа", contact_email="info@textilprom.ru")
    s2 = Supplier(name="Стиль+Пошив", description="Мастерская по пошиву одежды", contact_email="sales@stylesew.ru")
    db.add_all([s1, s2])
    db.commit()
    p1 = Product(name="Футболка хлопковая", description="100% хлопок, плотность 180г/м2", price=450, moq=50, supplier_id=s1.id, image="")
    p2 = Product(name="Джинсы мужские", description="Деним, классический крой", price=1200, moq=30, supplier_id=s2.id, image="")
    p3 = Product(name="Рюкзак городской", description="Нейлон, 20 л", price=900, moq=10, supplier_id=s1.id, image="")
    db.add_all([p1,p2,p3])
    db.commit()
    db.close()

if __name__ == "__main__":
    seed()