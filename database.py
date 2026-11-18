from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine(
    "mysql+pymysql://root@127.0.0.1:3306/DNApice?charset=utf8mb4"
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
