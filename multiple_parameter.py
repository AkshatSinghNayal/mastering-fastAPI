from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

#path + query param  

users =[]

class User(BaseModel):
    name : str
    age : int 


@app.post("/create-user")
def create_user(u : User) -> dict:
    users.append(u)
    return {
        "message" : "user created",
        "data" : u
    }


@app.put("/update/{id}")
def update_data( id : int , user : User ,  notify : bool = False) ->dict:
    if id < len(users):
        users[id] = user
        return{
            "message" : "user updated",
            "notify" : notify,
            "data" : user
        }
    raise HTTPException(status_code=404 , detail= "NOT FOUND")
