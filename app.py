from fastapi import FastAPI
from strawberry.asgi import GraphQL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from envs import env
from dotenv import load_dotenv
import strawberry


# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Cria uma instância do SQLAlchemy Engine
DATABASE_URL = env("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# Cria uma função para criar uma sessão do SQLAlchemy
def create_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

# Cria uma instância do aplicativo FastAPI
app = FastAPI()

# Importe do esquema GraphQL do arquivo resolvers.py
from resolvers.resolvers import combined_query, mutation_dvd

# Combinando os resolvers para manter apenas um endpoint
schema = strawberry.Schema(query=combined_query, mutation=mutation_dvd)

# Define o endpoint GraphQL
app.add_route("/graphql", GraphQL(schema))



# Rota de exemplo para testar a conexão com o banco de dados
@app.get("/")
async def read_root():
    db = create_session()
    try:
        result = db.execute("SELECT 1")
        return {"message": "Conexão com o banco de dados estabelecida com sucesso!"}
    except Exception as e:
        return {"message": f"Erro ao conectar ao banco de dados: {str(e)}"}
    finally:
        db.close()
