from datetime import datetime
import random , string
from traceback import format_exc
from fastapi import Depends, FastAPI, Response
from fastapi.responses import RedirectResponse
from fastapi.requests import Request
from base_models import url_req,Expired_url
from sqlalchemy.orm import Session
from constant import ENV,self_url
from buisness.url_shortner import validate_data,url_foramter
from traceback import format_exc
import model
from buisness.database_handler import Base, SessionLocal,engine
from buisness.crud import add_url_data, get_org_url_from_key, incr_counter_visit
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates") 

model.Base.metadata.create_all(bind=engine)
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(
    title="Url shortner",
    description="Get short url with customize message and keys",
    version="1.0.0"
)

@app.get("/")
def read_root(request : Request):
    from constant import self_url
    self_url = request.url
    print(self_url)
    return templates.TemplateResponse("url_page.html",{"request":request,"self_url":self_url})

@app.get("/{key:path}")
async def redirect_url_to_orginal(key:str,db:Session=Depends(get_db)):
    """
    With help of unique key we saved, it will redirect to original url.
    """
    try:
        url = self_url
        data = get_org_url_from_key(key)
        if not data:
            raise Exception("No matching url data found")
        if data.key:
            #update counter for each visit
            if datetime.strptime(str(data.expire_date),"%Y_%m_%d-%I:%M:%S_%p")<datetime.now():
                raise Expired_url("Url has been expired.")
            elif bool(data.one_time_use) and data.visit_counter>1:
                raise Expired_url("Url was for one time used,it has been expired.")
            else:
                incr_counter_visit(key,data.visit_counter)
            url = data.orginal_url
            if "https://" not in url:
                url = "https://"+url
        return RedirectResponse(url)
    except Expired_url as e:
        print(format_exc(),self_url)
        return RedirectResponse(self_url,status_code=200,headers={"message":"url is expired or deleted"})
    except Exception as e:
        print(format_exc(),self_url)
        return RedirectResponse(self_url,status_code=200,headers={"message":"Not redirected"})
    

#view api to use from web
@app.post("/quick_link")
async def genrate_url(url_data : url_req,request : Request,db:Session=Depends(get_db)):
    """
    url : required to genrate hash url and redirect to original site
    \n message : if you need to give message in genrated url 
        \n\t eg. ?message=special_link_for_user1
    \n special_key : if you want url to have unquie key from your side 
        \n\t eg. /special_offer_diwali
    \n expiry in day : its optional you can set your url expiry after n days , min - 1 ,max -30 , default 5
    """
    # print(url_data)
    try:
        # url_used = request.url
        # print(">>",url_used,request.json())
        url_data = validate_data(url_data)
        key = ''.join(random.sample((string.ascii_uppercase + string.ascii_lowercase + string.digits)*5,12))
        url_data["key"]=key
        save = add_url_data(db,url_data)
        return url_foramter(key,self_url)
    except Exception as e:
        from traceback import format_exc
        print(format_exc())
        return Response({"message":"something went wrong"})
