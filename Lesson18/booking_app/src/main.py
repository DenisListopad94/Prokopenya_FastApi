import random
from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, validator, PositiveInt, Field, constr
from typing_extensions import Literal

app = FastAPI()


@app.get("/")
def random_numbers():
    result_numbers = []
    for val in range(6):
        result_numbers.append(random.randint(0, 10))
    return result_numbers


@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}


@app.get("/item")
def get_query_types(item_id: int, name: str,) -> dict:
    return {"item_id": item_id, "name": name}


@app.get("/{name}")
def get_types(name: str, id_: int, age: int) -> dict:
    return {"name": name, "item_id": id_, "age": age}

# Используя pydantic создайте класс Actor c полями (actor_id int, name str, surname str, age int, sex str)
# Создайте эндпоинт c post запросом который принимает в body (actor: Actors).
# и возвращает актёра с переданными полями в теле запроса.


class Actor(BaseModel):
    actor_id: int
    name: str
    surname: str
    age: int
    sex: str
    email: EmailStr


@app.post("/{tr}")
def data_actor(actor: Actor) -> Actor:
    return actor


# Используйте возможности pydantic и провалидируйте поля класса Actor следующим образом:
# actor_id сделайте положительным числом, age определите от 0 до 100, name и surname сделайте не более 20 символов
# и не менее 2, sex добавьте возможность выбора только male и female .

class ActorTwo(BaseModel):
    actor_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: Literal["male", "female"]
    email: EmailStr


@app.post("/{actors_two}")
def data_actor_validated(actor_two: ActorTwo) -> ActorTwo:
    return actor_two
