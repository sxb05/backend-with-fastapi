from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
from .config import settings

                                                                                                                                                                                                                                                                                    # while True:
                                                                                                                                                                                                                                                                                    #     try:
                                                                                                                                                                                                                                                                                    #         conn = psycopg.connect("dbname=fastapi user=postgres password=12345678" , row_factory=dict_row)
                                                                                                                                                                                                                                                                                    #         cur = conn.cursor()
                                                                                                                                                                                                                                                                                    #         break
                                                                                                                                                                                                                                                                                    #     except Exception as error:
                                                                                                                                                                                                                                                                                    #         print("Error") 
                                                                                                                                                                                                                                                                                    #         time.sleep(20)    

                                                                                                                                                                                                                                                                                        









engine = create_engine(f"postgresql+psycopg2://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}")
                                                                             

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()