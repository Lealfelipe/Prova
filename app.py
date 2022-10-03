from datetime import date
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
    data_adesao = Column(date)

class Artista(Base):
    __tablename__ = "Artista"
    id_artista = Column(Integer, primary_key=True, unique=True)
    nome = Column(String(150), nullable=False)

class Musica(Base):
    __tablename__ = "Musica"
    id_musica = Column(Integer, primary_key=True, unique=True)
    nome_musica = Column(String(150), nullable=False)
    id_cantor = Column(Integer)
    id_compositor = Column(Integer)

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
    id_banda = Column(Integer, primaryKey=True)
    nome_banda = Column(String(150))

class Participa(Base):
    __tablename__ = "Participa"
    id_participa = Column(Integer, primary_key=True)
    id_banda = Column(Integer)
    id_instrumentista = Column(Integer)

class Canta(Base):
    __tablename__ = "Participa"
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

    with Session.begin() as session:
        carteira = CarteiraOMB(date="2001/05/03")
        id_carteira = carteira.id_carteira
        session.add(carteira)

    with Session.begin() as session:
        artista = Artista(nome="Chorão")
        id_artista = artista.id_artista
        session.add(artista)
        
    with Session.begin() as session:
        cantor = Cantor.id_artista=1
        cantor = Cantor.id_musica=1
        id_cantor = Cantor.id_cantor
        session.add(cantor)

    with Session.begin() as session:
        compositor = Compositor.id_artista=1
        compositor = Compositor.id_musica=1
        id_compositor = Compositor.id_compositor
        session.add(compositor)
    

    with Session.begin() as session:
        musica = Musica(nome_musica="Ela vai voltar")
        id_musica = musica.id_musica        
        id_cantor = musica.id_cantor
        id_compositor = musica.id_compositor
        session.add(musica)

    with Session.begin() as session:
        disco = Disco.id_musica=1
        disco = Disco.id_banda=1
        id_disco = Disco.id_disco
        session.add(disco)

    with Session.begin() as session:
        banda = Banda(nome="Charlie Brown Jr.")
        id_banda = banda.id_banda
        session.add(banda)

    with Session.begin() as session:
        participa = Participa.id_banda=1
        participa = Participa.id_instrumentista=1
        id_participa = Participa.id_participa
        session.add(participa)

    with Session.begin() as session:
        canta = Canta.id_banda=1
        canta = Canta.id_cantor=1
        id_canta = Canta.id_canta
        session.add(canta)

    with Session.begin() as session:
        instrumentista = Instrumentisa.id_artista=1
        instrumentista = Instrumentisa.id_instrumento=1
        id_instrumentista = Instrumentisa.id_instrumentista
        session.add(instrumentista)

    with Session.begin() as session:
        instrumento = Instrumento(nome_instrumento=("Guitarra"))
        id_instrumento = instrumento.id_instrumento
        session.add(instrumento)





    

    

if __name__ == "__main__":
    main()