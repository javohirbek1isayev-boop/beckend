
from pydantic import BaseModel, ConfigDict

class UserCreate(BaseModel):
    telegram_id: int
    first_name: str | None = None
    username: str | None = None

class UserResponse(UserCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TaskCreate(BaseModel):
    title: str
    user_id: int

class TaskResponse(TaskCreate):
    id: int
    completed: bool

    model_config = ConfigDict(from_attributes=True)
