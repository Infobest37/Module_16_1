from fastapi import FastAPI
from pydantic import BaseModel
# Создаем экземпляр приложения FastAPI
app = FastAPI()

# Определение базового маршрута
@app.get("/")
async def root():
    return {"Главная страница"}
@app.get("/user/admin")
async def admin():
    return {"Вы вошли как администратор"}

@app.get("/user/{password}")
async def news(password: int) -> dict:
    return {"message": f"Вы вошди как пользователь № {password}"}

@app.get("/users")
async def user(username: str, age: int) -> dict:
     return {"Информация о пользователе. Имя": username, "Возраст": age}