        # database.py
# Helps setup database connection and provide foundational components for ORM
# Centralizes DB setup, making it reusable across the app for sessions and models
        # create_engine():
# Establishes the connection to the database
# Here, it connects to a SQLite file named test.db
        # connect_args:
# SQLite-specific to allow connection sharing across threads

    # sessionmaker:
# Helps create new database sessions
# Each session represents a transactional scope to the DB
    # autoflush=False:
# SQLAlchemy will not automatically flush changes to the DB unless explicitly committed or refreshed
    # autocommit=False:
# Disables automatic commit after each query
# Commit manually to control transactions

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
