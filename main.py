from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ToDo(BaseModel):
    id: int | None = None
    description: str


todos = []

## get all todos
@app.get("/todos")
async def get_todos():
    return {"ToDos": todos}

## get single todos
@app.get("/todos/{todo_id}")
async def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "not found"}


## create a todos
@app.post("/todos")
async def post_todos(todo:ToDo):
    if len(todos) == 0:
        todo.id = 1
    else:
        todo.id = todos[len(todos)-1].id+1
    todos.append(todo)
    return {"message": "done"}

## update a todos
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int, todo_obj : ToDo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_obj.id
            todo.description = todo_obj.description
            return {"message": "updated"}
    return {"message": "not found"}

## delete a todos
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "deleted"}
    return {"message": "not found"}