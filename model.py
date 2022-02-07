from sqlalchemy import Boolean, Column, Integer, String
from buisness.database_handler import Base

class url_data(Base):
    __tablename__ = "url_data"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True, nullable=False)
    orginal_url=Column(String, index=True, nullable=False)
    special_key=Column(String(255), index=True, nullable=False)
    key=Column(String(255), index=True, nullable=False)
    message = Column(String(100), index=True, nullable=True)
    expire_date = Column(String, index=True, nullable=False)
    email = Column(String,index=True,nullable=True)
    one_time_use = Column(Boolean,index=True,nullable=False)
    visit_counter = Column(Integer,nullable=False)