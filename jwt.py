from fastapi import FastAPI, HTTPException, Header, Depends
from jose import jwt
from datetime import datetime, timedelta, timezone

app = FastAPI()

SECRET_KEY = "ABC"
ALGORITHM = "HS256"


def create_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(days=30)

    to_encode.update({
        "exp": expire
    })

    token = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


@app.post("/login")
def login(username: str, password: str):

    if username != "admin" or password != "1234":
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_token({
        "sub": username
    })

    return {
        "access_token": token
    }


def verify_token(token: str = Header(None)):

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


@app.get("/secure")
def secure_data(user=Depends(verify_token)):

    return {
        "message": "secured data accessed",
        "user": user
    }