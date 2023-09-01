from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column

base = declarative_base()
class SampleTable(base):
    __tablename__ = "SampleTable"
    name = Column(String,primary_key=True)
    userID = Column(String)