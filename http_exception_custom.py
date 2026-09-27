from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi import Response , Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundException(Exception):
    def __init__(self, name : str ):
        self.name = name 


@app.exception_handler(UserNotFoundException)
def user_not_found( request : Request , exp : UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status" : "error ",
            "message" : "user not found " 
        }
    )


@app.get("/user/{name}")
def user_found(name : str ):
    if name != "mohit":
        raise UserNotFoundException(name)
     