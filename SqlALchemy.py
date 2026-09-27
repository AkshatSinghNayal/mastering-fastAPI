from sqlalchemy import create_engine,Column,Integer,String
from fastapi import FastAPI,Depends
from sqlalchemy.orm import sessionmaker , declarative_base,Session

app = FastAPI()

DATABASE_URL = "sqlite:///./test.dp"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread" : False }
)

sessionLocal = sessionmaker(bind = engine)

Base = declarative_base()

class TODO(Base):
    __tableName__ = "todos"

    id = Column(Integer,primary_key=True, index = True)
    title = Column(String)
    completed = Column(String)


Base.metadata.create_all(bind = engine)

def get_db():
    db=  sessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/")
def get_user( db : Session = Depends(get_db)):
    return {
        "message" : " DB connected Fine "
    }