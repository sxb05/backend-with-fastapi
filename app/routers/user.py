from ..schemas import  User, UserOut
from fastapi import Body, FastAPI,HTTPException,status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import Base, engine, SessionLocal, get_db
from ..utils import hash_password
from .. import models
from typing import List


router = APIRouter(

    prefix="/Users",
    tags=["users"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserOut)
def create_products(user: User, db: Session = Depends(get_db)):
    new_pass = hash_password(user.password)
    user.password = new_pass
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 


@router.get("/{id}", response_model=UserOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")
    return user

@router.get("/", response_model=List[UserOut])
def get_users(db: Session = Depends(get_db)):
    all_user = db.query(models.User).all()
    return all_user

