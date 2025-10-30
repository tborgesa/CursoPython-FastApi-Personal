from sqlalchemy import MetaData, create_engine, Engine
from sqlalchemy.orm import declarative_base, sessionmaker

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

db: Engine = create_engine("sqlite:///C:\\FontesGitHub\\CursoPython-FastApi-Personal\\database\\banco.db")

metadata = MetaData(naming_convention=convention)
Base = declarative_base(metadata=metadata)

def get_session():
    try:
        Session: sessionmaker = sessionmaker(bind=db)
        session = Session()
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()