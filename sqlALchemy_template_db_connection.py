from fastapi import FastAPI, Depends, Request
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session


app = FastAPI()

#DB Creation
DATABASE_URL = "sqlite:///./test.db"

#DB Engine which talks to the database for communication purpose 
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False}
)

#Session factory for accessing the DB by any req later 
sessionLocal = sessionmaker(bind=engine)

#Base class for database model -> this is like which class inherits from me can act as a database table
Base = declarative_base()


#DB table
class TODO(Base):
    __tablename__ = "Todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(String)

#create Table
Base.metadata.create_all(bind=engine)

#DB dependency to get new session everytime
def get_db():
    db = sessionLocal()

    try:
        yield db
    finally:
        db.close()


#api endpoint
@app.get("/home")
def get_todos(db : Session = Depends(get_db)):
    todos = db.query(TODO).all()
    return todos