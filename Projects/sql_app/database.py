#importing the SQlalchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#creating a database url
SQLALCHEMY_DATABASE_URL = "postgresql://librarian:password@postgreserver/library"

#creating SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#creating a "sessionLocal" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creating a base
Base = declarative_base()

