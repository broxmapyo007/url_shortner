
import model
from sqlalchemy.orm import Session

from buisness.database_handler import SessionLocal

def get_org_url_from_key(key: str):
    db = SessionLocal()
    return db.query(model.url_data).filter(model.url_data.key==key).first()

def incr_counter_visit(key: str,counter:int):
    url_db = model.url_data()
    db = SessionLocal()
    db.query(model.url_data).filter(model.url_data.key==key).update({"visit_counter":counter+1})
    db.commit()
    return True

    
def add_url_data(db:Session,data_req):
    url_db = model.url_data()
    # print(data_req)
    url_db.key=data_req["key"]
    url_db.orginal_url=data_req["original_url"]
    url_db.message=",".join(data_req["message"])
    url_db.special_key=data_req["special_key"]
    url_db.email = data_req["email"]
    url_db.expire_date=data_req["expire_date"]
    url_db.one_time_use = data_req["one_time_use"]
    url_db.visit_counter=0
    db.add(url_db)
    db.commit()
    # print(">>save",url_db.id)
    return True

