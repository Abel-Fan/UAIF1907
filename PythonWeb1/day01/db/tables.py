from .database import Base
from sqlalchemy import Integer,String,Column
# Integer 整型   String VarChar  Column 字段

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer,primary_key=True)  # primary_key 主键
    num = Column(String)
    username = Column(String)
    age = Column(Integer)
    sex = Column(Integer)

