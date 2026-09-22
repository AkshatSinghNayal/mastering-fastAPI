from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

todos = []

class TODO(BaseModel):
    id:int
    title: str
    description: str
    completed: bool = False



@app.post("/todos")
def add_todo(todo: TODO) -> dict:
    todos.append(todo)
    return {
        "message": "TODO item added successfully",
        "data": todo   
    }


@app.get("/todos")
def get_todos() -> dict:
    return {
        "message": "TODO items retrieved successfully",
        "data": todos
    }


@app.get("/todos/{id}")
def get_todo_by_id(id: int) ->dict:
    for it in todos:
        if it.id == id:
            return {
                "message": "TODO item retrieved successfully",
                "data": it  
            }
    raise HTTPException(status_code=404, detail="TODO item not found")


@app.put("/update/{id}")
def update_todo( id : int , updated_todo: TODO) ->dict:
    for index , element in enumerate(todos):
        if element.id == id:
            todos[index] = updated_todo
            return {
                "message": "TODO item updated successfully",
                "data": updated_todo  
            }
    raise HTTPException(status_code=404, detail="TODO item not found")


@app.delete("/delete/{id}")
def delete_by_id(id : int )->dict:
    for index, ele in enumerate(todos):
        if ele.id == id:
            todos.pop(index)
            return{
                "message" : "deleted"
            }
    raise HTTPException(status_code=404 , detail=" ID NOT FOUND ! ")