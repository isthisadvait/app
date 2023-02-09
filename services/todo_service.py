from typing import List
from app.models.user_model import User
from app.models.todo_model import Todo
from app.schemas.todo_schema import TodoCreate
from uuid import UUID
class TodoService:
    @staticmethod
    async def list_todos(user:User)->List[Todo]:
        todos = await Todo.find(Todo.owner.id == user.user_id).to_list()
        return todos

    @staticmethod
    async def create_todo(user:User,data:TodoCreate):
        todo = Todo(**data.dict(),owner = user)
        return await todo.insert()

    @staticmethod
    async def retrieve_todo(current_user:User,todo_id:UUID):
        todo = await Todo.find_one(Todo.todo_id == todo_id,Todo.owner.id == current_user.id)
        return todo

