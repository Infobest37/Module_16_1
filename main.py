from fastapi import FastAPI
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"message": "Hello Worl"}


@app.get("/usertest/A/B")
async def news() -> dict:
    return {"message": f"Привет я свой"}


@app.get("/user/{first_name}/{last_name}")
async def news(first_name: str, last_name: str) -> dict:
    return {"message": f"Hello {first_name} {last_name}"}

@app.get("/id")
async def news_id(username: str, age: int) -> dict:
    return {"User": username, "Age": age}


