from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Basic SQLAlchemy setup using a sqlite file in the instance folder for local development
Base = declarative_base()
engine = create_engine('sqlite:///instance/octofit.db', echo=False)
SessionLocal = sessionmaker(bind=engine)
