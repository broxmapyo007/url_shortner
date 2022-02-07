from fastapi import Path
from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

class url_req(BaseModel):
    original_url : str = "" #"https://www.google.com"
    special_key : Optional[str] = ""
    message : Optional[list] = []
    email : EmailStr #= ""
    expire_date: Optional[int] = 5
    one_time_use:bool = False

#exception class
class Expired_url(Exception):
    pass
