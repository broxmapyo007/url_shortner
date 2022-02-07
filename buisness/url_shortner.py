
from datetime import datetime,timedelta

from buisness.crud import get_org_url_from_key
from sqlalchemy.orm import Session

def url_foramter(key,self_url):
    val_ = get_org_url_from_key(key)
    self_url = "/".join(str(self_url).split("/")[0:3:2])
    url_format = self_url+f"/{str(val_.key)}"
    if val_.special_key:
        special_key = val_.special_key
        url_format += f"/{special_key}"
    if val_.message:
        msg_data=val_.message.split(",")
        msg = ""
        for ind,m in enumerate(msg_data):
            if m!="string":
                msg+=f"?message{ind+1}={m}"
        url_format+= f"{msg}"
    return {"short_url":url_format}

def validate_data(ud):
    data = {}
    data["original_url"] = ud.original_url if ud.original_url!="string" else ""
    data["special_key"] = ud.special_key if ud.special_key!="string" else ""
    data["message"] = [str(i) for i in ud.message]
    data["one_time_use"] = ud.one_time_use
    data["email"]=ud.email
    ex_date = datetime.now() + timedelta(days=5)
    if ud.expire_date and 0<int(ud.expire_date)<31:
        ex_date = datetime.now() + timedelta(days=int(ud.expire_date))
    data["expire_date"] = datetime.strftime(ex_date,"%Y_%m_%d-%I:%M:%S_%p")
    return data