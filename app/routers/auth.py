from fastapi import APIRouter, FastAPI, HTTPException, status, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from..schemas import Login
from ..utils import verify_password
router = APIRouter(tags=["auth"])


@router.post("/login")
def login(log_cred: Login, db: Session = Depends(get_db), response_model=LoginOut):
    user_login = db.query(models.User).filter(models.User.email == log_cred.email).first()
    if not user_login:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with email {log_cred.email} not found")
    if not verify_password(log_cred.password, user_login.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"invalid password")

    
    
    return user_login