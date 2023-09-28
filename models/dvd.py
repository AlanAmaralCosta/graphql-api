from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Dvd(Base):
    __tablename__ = "tbl_dvds"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)
    release_year = Column(Integer)
    genre = Column(String)
