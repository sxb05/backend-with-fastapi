from ..schemas import  User, UserOut
from fastapi import Body, FastAPI,HTTPException,status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import Base, engine, SessionLocal, get_db
from typing import List
from ..schemas import Product, ProductOut
from .. import models
from ..oauth2 import get_current_user
router = APIRouter(

    prefix="/products",
    tags=["products"]
)












#@router = FastAPI()
# models.Base.metadata.create_all(bind=engine)

# # Mount frontend static files (served from@router/frontend)
# #@router.mount("/static", StaticFiles(directory=@router/frontend"), name="static")




# while True:
#     try:
#         conn = psycopg.connect("dbname=fastapi user=postgres password=12345678" , row_factory=dict_row)
#         cur = conn.cursor()
#         break
#     except Exception as error:
#         print("Error") 
#         time.sleep(20)    

@router.get("/", response_model= List[ProductOut])
def get_products(db: Session = Depends(get_db), get_currentuser: int = Depends(get_current_user),limit:int = 10,skip: int = 0):
    product_query = db.query(models.Products).filter(models.Products.owner_id == get_currentuser.id).limit(limit).offset(skip).all()
    
   

    return  product_query


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= ProductOut)
def create_products(product: Product, db: Session = Depends(get_db), get_currentuser: int = Depends(get_current_user)):
    # new_product = models.Products(name=product.name, price=product.price, inventory=product.inventory)
    
    print(get_currentuser.email)
    
    new_product = models.Products(owner_id = get_currentuser.id,**product.dict())

    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product 

@router.get("/{id}", response_model=List[ProductOut])
def get_product(id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    product = db.query(models.Products).filter(models.Products.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id {id} not found")
    return product




@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id: int, db: Session = Depends(get_db),user_id: int = Depends(get_current_user)):
    product_query = db.query(models.Products).filter(models.Products.id == id)
    product = product_query.first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id {id} not found")
    
    if product.owner_id!= user_id.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    
    product_query.delete(synchronize_session=False)
    
    db.commit()
    return { f"product with id {id} deleted successfully"}   


@router.put("/{id}", response_model=ProductOut)
def update_product(id: int, product: Product, db: Session = Depends(get_db), get_currentuser: models.User = Depends(get_current_user)):
    product_query = db.query(models.Products).filter(models.Products.id == id)
    product_db = product_query.first()
    if not product_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"product with id {id} not found")
    if product_db.owner_id != get_currentuser.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform requested action")
    product_query.update(product.dict(), synchronize_session=False)
    db.commit()
    return { "updated successfully"}