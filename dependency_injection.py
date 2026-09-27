# dependency injection
from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )
    return {
        "user" : "authorized"
    }

# def common_logic():
#     return{
#         "message" : "common logic executed"
#     }

# @app.get("/home")
# def home(data = Depends(common_logic)):
#     return data


@app.get("/user-verify")
def verify( token : str = Depends(verify_token)):
    return {
        "message" : "secure data accessed",
        "user" : token 
    }