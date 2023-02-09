from fastapi import APIRouter,Depends
from app.schemas.todo_schema import TodoOut,TodoCreate
from app.models.user_model import User
from app.services.todo_service import TodoService
from app.models.todo_model import Todo
from uuid import UUID
todo_router = APIRouter()

@todo_router.get('/',summary="Get all todos of the user",response_model=TodoOut)
async def List(current_user:User = Depends(get_current_user)):
     return await TodoService.list_todos(current_user)


@todo_router.post('/create',summary="Create Todo",response_model=Todo)
async def create_todo(data:TodoCreate,current_user:User = Depends(get_current_user)):
    return await TodoService.create_todo(data,current_user)

@todo_router.get('/{todo_id}',summary="Get a todo by todo_id",response_model=TodoOut)
async def retrieve(todo_id:UUID,current_user:User = Depends(get_current_user)):
    return await TodoService.retrieve_todo(current_user,todo_id)
