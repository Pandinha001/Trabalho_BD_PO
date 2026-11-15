from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

### criando a conexão (troque pelos seus dados)
### formato: mysql+pymysql://USUARIO:SENHA@HOST:PORTA/BANCO
engine = create_engine(
    "mysql+pymysql://root:sua_senha@localhost:3306/DNApice?charset=utf8mb4"
)

Base = declarative_base()
Session = sessionmaker(bind=engine)
