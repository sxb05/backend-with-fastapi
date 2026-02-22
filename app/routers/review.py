# import models
# from sqlalchemy.orm import Session
# from fastapi import Body, FastAPI,HTTPException,status, Depends, APIRouter
# from ..database import Base, engine, SessionLocal, get_db
# from .. import oauth2
# router = APIRouter(

#     prefix="/review",
#     tags=["review"]

# )




# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create_review(review: models.Review, db: Session = Depends(get_db)):
#     new_review = models.Review(**review.dict())
#     db.add(new_review)
#     db.commit()
#     db.refresh(new_review)
#     return new_review