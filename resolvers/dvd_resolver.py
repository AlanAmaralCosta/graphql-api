from typing import List, Optional
import strawberry
from app import create_session
from models.dvd import Dvd

@strawberry.type
class DVDType:
    id: int
    title: str
    director: str
    release_year: int
    genre: str

@strawberry.type
class Query:
    dvds: List[DVDType] = strawberry.field(resolver=lambda info: Query.resolve_dvds(info))
    
    # Query para selecionar por ID
    @strawberry.field
    async def dvd_by_id(self, info, id: int) -> Optional[DVDType]:
        db = create_session()
        dvd = db.query(Dvd).filter(Dvd.id == id).first()
        db.close()
        return dvd
    
    # Query para selecionar por titulo
    @strawberry.field
    async def dvds_by_title(self, info, title: str) -> List[DVDType]:
        db = create_session()
        dvds = db.query(Dvd).filter(Dvd.title.ilike(f'%{title}%')).all()
        db.close()
        return dvds
    
    # Query para selecionar tudo
    @staticmethod
    async def resolve_dvds(info) -> List[DVDType]:
        db = create_session()
        dvds = db.query(Dvd).all()
        db.close()
        return dvds

    # Resolver
    @staticmethod
    async def resolve_dvd_by_id(info, id: int) -> Optional[DVDType]:
        db = create_session()
        dvd = db.query(Dvd).filter(Dvd.id == id).first()
        db.close()
        return dvd

    # Resolver
    @staticmethod
    async def resolve_dvds_by_title(info, title: str) -> List[DVDType]:
        db = create_session()
        dvds = db.query(Dvd).filter(Dvd.title.ilike(f'%{title}%')).all()
        db.close()
        return dvds

@strawberry.type
class Mutation:
    # Mutation para criar um DVD
    @strawberry.mutation
    async def create_dvd(info, title: str, director: Optional[str] = None, release_year: Optional[int] = None, genre: Optional[str] = None) -> DVDType:
        db = create_session()
        dvd = Dvd(title=title, director=director, release_year=release_year, genre=genre)
        db.add(dvd)
        db.commit()
        db.refresh(dvd)
        db.close()
        return dvd

    # Mutation para atualizar um DVD pelo ID
    @strawberry.mutation
    async def update_dvd(info, id: int, title: str, director: Optional[str] = None, release_year: Optional[int] = None, genre: Optional[str] = None) -> DVDType:
        db = create_session()
        dvd = db.query(Dvd).filter(Dvd.id == id).first()
        
        if dvd:
            dvd.title = title
            dvd.director = director
            dvd.release_year = release_year
            dvd.genre = genre
            db.commit()
            db.refresh(dvd)
        
        db.close()
        return dvd

    # Mutation para excluir um DVD pelo ID
    @strawberry.mutation
    async def delete_dvd(info, id: int) -> bool:
        db = create_session()
        dvd = db.query(Dvd).filter(Dvd.id == id).first()
        
        if dvd:
            db.delete(dvd)
            db.commit()
            db.close()
            return True
        
        db.close()
        return False
