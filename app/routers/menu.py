from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.menu import Menu
from app.schemas.menu import MenuCreate, MenuResponse
from app.security.roles import admin_only, staff_or_admin

router = APIRouter(prefix="/menu", tags=["Menu"])

@router.post("/", dependencies=[Depends(admin_only)])
def create_item(item: dict, db: Session = Depends(get_db)):
    return {"message": "Item added"}


@router.get("/", dependencies=[Depends(staff_or_admin)])
def list_items(db: Session = Depends(get_db)):
    return {"items": ["Cappuccino", "Latte", "Espresso"]}



@router.post("/", response_model=MenuResponse,
             dependencies=[Depends(admin_only)])
def add_menu(
    item: MenuCreate,
    db: Session = Depends(get_db)
):
    menu = Menu(name=item.name, price=item.price)
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu

@router.get("/")
def get_menu(db: Session = Depends(get_db)):
    return db.query(Menu).all()
