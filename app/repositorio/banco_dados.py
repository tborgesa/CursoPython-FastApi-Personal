from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db = create_engine("sqlite:///C:\\FontesGitHub\\CursoPython-FastApi-Personal\\database\\banco.db")
Base = declarative_base()

def get_session():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()