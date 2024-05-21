from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schema import list_serial
# from bson import objectId

router = APIRouter()

#get request method
@router.get("/")
async def get_todos():
    todos= list_serial(collection_name.find())
    return todos

#post request method
@router.post("/")
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))

#put request method
@router.put("/{id}")
async def put_todo(id:str,todo:Todo):
    collection_name.find_and_update({"_id":object(id)},{"$set":dict(todo)})

#delete request method
@router.delete("/{id}")
async def delete_todo(id:str):
    collection_name.find_and_delete({"_id":object(id)})

