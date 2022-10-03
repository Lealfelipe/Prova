from datetime import date, datetime
from enum import unique
from msvcrt import kbhit
from sqlite3 import Date
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


URL = "mysql+mysqlconnector://root:1903Imortal@localhost/PROVA"

Base = declarative_base()

class CarteiraOMB(Base):
    __tablename__ = "CarteiraOMB"
    id_carteira = Column(Integer, primary_key=True, unique=True)
    data_adesao = Column(String(150))

class Artista(Base):
    __tablename__ = "Artista"
    id_artista = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(150), nullable=False)

class Musica(Base):
    __tablename__ = "Musica"
    id_musica = Column(Integer, primary_key=True, unique=True)
    nome_musica = Column(String(150), nullable=False)
    

class Cantor(Base):
    __tablename__ = "Cantor"
    id_cantor = Column(Integer, primary_key=True)
    id_artista = Column(Integer)
    id_musica = Column(Integer)

class Compositor(Base):
    __tablename__ = "Compositor"
    id_compositor = Column(Integer, primary_key=True)
    id_artista = Column(Integer)
    id_musica = Column(Integer)

class Disco(Base):
    __tablename__ = "Disco"
    id_disco = Column(Integer, primary_key=True)
    id_banda = Column(Integer)
    id_musica = Column(Integer)

class Banda(Base):
    __tablename__ = "Banda"
    id_banda = Column(Integer, primary_key=True, unique=True)
    nome_banda = Column(String(150), nullable=False)

class Participa(Base):
    __tablename__ = "Participa"
    id_participa = Column(Integer, primary_key=True, unique=True)
    id_banda = Column(Integer)
    id_instrumentista = Column(Integer)

class Canta(Base):
    __tablename__ = "Canta"
    id_canta = Column(Integer, primary_key=True)
    id_cantor = Column(Integer)
    id_banda = Column(Integer)

class Instrumentisa(Base):
    __tablename__ = "Instrumentista"
    id_instrumentista = Column(Integer, primary_key=True)
    id_artista = Column(Integer)
    id_instrumento = Column(Integer)

class Instrumento(Base):
    __tablename__ = "Instrumento"
    id_instrumento = Column(Integer, primary_key=True)
    nome_instrumento = Column(String(150))


def main():
    engine = create_engine(url=URL)
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(engine, expire_on_commit=False)

if __name__ == "__main__":
    main()