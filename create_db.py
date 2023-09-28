from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# URL de conexão com o banco de dados
db_url = "postgresql://seu_usuario:senha@localhost:5432/api_graphql_postgres_1"

# Cria a instância do SQLAlchemy Engine
engine = create_engine(db_url)

# Cria a sessão do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Define a classe para o modelo de DVD
Base = declarative_base()

class DVD(Base):
    __tablename__ = 'tbl_dvds'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    director = Column(String(255))
    release_year = Column(Integer)
    genre = Column(String(100))

# Cria a tabela se ela não existir
Base.metadata.create_all(engine)

# Gere uma carga de 15 DVDs
for i in range(1, 16):
    dvd = DVD(
        title=f"DVD {i}",
        director=f"Director {i}",
        release_year=2000 + i,
        genre=f"Genre {i}"
    )
    session.add(dvd)

# Commit das mudanças no banco de dados
session.commit()

# Fecha a sessão
session.close()
