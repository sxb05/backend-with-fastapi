from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


                                                                                                                                                                                                                                                                                    # while True:
                                                                                                                                                                                                                                                                                    #     try:
                                                                                                                                                                                                                                                                                    #         conn = psycopg.connect("dbname=fastapi user=postgres password=12345678" , row_factory=dict_row)
                                                                                                                                                                                                                                                                                    #         cur = conn.cursor()
                                                                                                                                                                                                                                                                                    #         break
                                                                                                                                                                                                                                                                                    #     except Exception as error:
                                                                                                                                                                                                                                                                                    #         print("Error") 
                                                                                                                                                                                                                                                                                    #         time.sleep(20)    

                                                                                                                                                                                                                                                                                        









engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/fastapi")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()