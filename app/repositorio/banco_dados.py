from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///C:\\FontesGitHub\\CursoPython-FastApi-Personal\\database\\banco.db")
Base = declarative_base()