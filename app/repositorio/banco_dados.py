from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker

db: Engine = create_engine("sqlite:///C:\\FontesGitHub\\CursoPython-FastApi-Personal\\database\\banco.db")
Base = declarative_base()

def get_session():
    try:
        Session: sessionmaker = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()