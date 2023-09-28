# Importe as bibliotecas necessárias
import strawberry
from strawberry.types import Info
from typing import List
from app import create_session

from models.dvd import Dvd

# Define o tipo GraphQL para o modelo User
@strawberry.type
class DvdType:
    id: int
    title: str
    director: str
    release_year: int
    genre: str

# Defina a consulta GraphQL para listar todos os usuários diretamente na classe Query
@strawberry.type
class Query:
    dvdss: List[DvdType] = strawberry.field(
        resolver=lambda info: Query.resolve_dvds(info)
    )

    @staticmethod
    async def resolve_dvds(info: Info) -> List[DvdType]:
        db = create_session()
        dvds = db.query(Dvd).all()
        db.close()
        return dvds

# Crie o esquema GraphQL
schema = strawberry.Schema(query=Query)
