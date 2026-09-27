from fastapi import FastAPI, Depends, HTTPException
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

#creating api
@app.post("/todo")
def create_post(title:str , db : Session = Depends(get_db)):
    todo = TODO( title = title , completed = "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)

    return {
        "message" : "todo-created",
        "data" : todo
    }


#read all data
@app.get("/all")
def fetch_all( db : Session = Depends(get_db)):
    todo = db.query(TODO).all()
    return {
        "total" : len(todo),
        "data"  : todo          
    }

@app.get("/based/{id}")
def get_by_id(id : int , db : Session = Depends(get_db)): 
    todo = db.query(TODO).filter(TODO.id == id ).first()

    if not todo:
        raise HTTPException(status_code=404 , detail=" todo not found ")
    return {
        "data" : todo
    }


@app.put("/update/{id}")
def update_by_id( id : int , title : str , db : Session = Depends(get_db)):
    todo = db.query(TODO).filter(TODO.id == id ).first()

    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found to update")


    todo.title = title
    db.commit()
    db.refresh(todo)

    return {
        "message" : "todo updated successfully",
        "data" : todo
    }





#delete
@app.delete("/delete/{id}")
def delete_by_id( id : int , db : Session = Depends(get_db)):
    todo = db.query(TODO).filter(TODO.id == id ).first()
    

    if not todo:
        raise HTTPException(status_code=404, detail="not found to delete")


    db.delete(todo)
    db.commit()
    all = db.query(TODO).all()

    return{
        "message" : "deleted",
        "data->" : all
    }