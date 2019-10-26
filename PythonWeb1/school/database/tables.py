from database.db import Base,session
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship

class Admins(Base):
    __tablename__ ="admins"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)

class Classes(Base):
    __tablename__ ="classes"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)
    teacher = relationship("Teachers")
    students = relationship("Students")

class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    num = Column(String)
    age = Column(Integer)
    sex = Column(Integer)
    cid = Column(Integer,ForeignKey("classes.id"))

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    num = Column(String)
    age = Column(Integer)
    sex = Column(Integer)
    cid = Column(Integer,ForeignKey("classes.id"))