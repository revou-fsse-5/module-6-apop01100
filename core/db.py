import os
from dotenv import load_dotenv
from sqlalchemy import URL, create_engine,  Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


load_dotenv()

connection_string = URL.create(
    'postgresql',
    username=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSWORD'),
    host=os.getenv('DB_HOST'),
    database=os.getenv('DB_NAME')
)

engine = create_engine(connection_string)

Base = declarative_base()

class Animals(Base):
    __tablename__ = 'animals'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    species = Column(String)
    age = Column(Integer)
    gender = Column(String)
    
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
