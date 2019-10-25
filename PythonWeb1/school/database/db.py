from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+pymysql://root:123456@127.0.0.1:3306/deme1?charset=utf8")
Session = sessionmaker(bind=engine)

# 会话
session = Session()
# 数据表基类
Base = declarative_base()



