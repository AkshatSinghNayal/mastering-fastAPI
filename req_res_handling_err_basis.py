from fastapi import FastAPI , status , HTTPException

app = FastAPI()

@app.post("/create_user" , status_code=status.HTTP_200_OK)
def create_user():
    return {
        "message" : "userCreated"
    }


@app.get("/user")
def user():
    return{
        "status" : "success",
        "message" : "this is custom response"
    }