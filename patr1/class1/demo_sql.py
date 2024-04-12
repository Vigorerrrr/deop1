from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# 创建数据库连接
DB_USER = 'root'
DB_PASSWORD = 'my123'
DB_HOST = '192.168.10.23'
DB_PORT = '3306'
DB_NAME = 'mytest'

# MySQL连接字符串格式：mysql://username:password@host:port/database_name
DB_URI = f'mysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8'
engine = create_engine(DB_URI, echo=True)  # echo=True 可以输出所有执行的SQL语句

# 创建模型基类
Base = declarative_base()

# 定义模型类
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    # 如果有外键关联，则可以通过relationship来定义关系
    # posts = relationship('Post', backref='author')

# 创建数据表
Base.metadata.create_all(engine)

# # 创建Session对象
# Session = sessionmaker(bind=engine)
# session = Session()
#
# # 创建数据
# user1 = User(name='Alice', age=30)
# session.add(user1)
# session.commit()
#
# # 查询数据
# user = session.query(User).filter_by(name='Alice').first()
# print(user.name, user.age)
#
# # 更新数据
# user.age = 31
# session.commit()
#
# # 删除数据
# session.delete(user)
# session.commit()


