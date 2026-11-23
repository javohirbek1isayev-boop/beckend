from fastapi import FastAPI

from database import engine, Base
import models

from routers import users, tasks

app = FastAPI(
    title="Telegram Task Manager API",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Task Manager API is running"
    }