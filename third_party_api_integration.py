from fastapi import FastAPI, HTTPException
import requests


# response = requests.get("https://jsonplaceholder.typicode.com/posts")

# data = response.json()
# print(data)


app = FastAPI()


@app.get("/all")
def get_all():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)    
    return response.json()


@app.get("/post/{id}")
def get_by_id(id:int):
    url = f"https://jsonplaceholder.typicode.com/posts/{id}"
    response = requests.get(url)    

    if response.status_code!=200:
        raise HTTPException(status_code=404 , detail="not found by id ")

    return response.json()

