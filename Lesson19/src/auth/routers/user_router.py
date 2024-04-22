from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.auth.schemas.user_schema import User
import re

router = APIRouter(
    prefix="/users",
    tags=["Auth"]
)

# router.mount("/static", StaticFiles(directory="static"), name="users")
router.mount("/static", StaticFiles(directory="static"), name="users")
templates = Jinja2Templates(directory="templates")


@router.post("/")
def data_actor_validated(user: User) -> User:
    return user


def is_alphanumeric(text):
    return re.search(r"^[a-zA-Z]", text) is not None


@router.get("/get_template", response_class=HTMLResponse)
def get_users(request: Request):
    # user = User.new(1, "Ivan", "Petov", 14, "male", "ivan@mail.ru")
    users = [{"id": 1, "name": "Александра", "surname": "Смирнова", "age": 25, "sex": "female",
              "email": "alexandra.smirnova@example.com"},
             {"id": 2, "name": "Максим", "surname": "Иванов", "age": 32, "sex": "male",
              "email": "maxim.ivanov@example.com"},
             {"id": 3, "name": "Екатерина", "surname": "Петрова", "age": 28, "sex": "female",
              "email": "ekaterina.petrova@example.com"},
             {"id": 4, "name": "Дмитрий", "surname": "Сидоров", "age": 41, "sex": "male",
              "email": "dmitriy.sidorov@example.com"},
             {"id": 5, "name": "Анна", "surname": "Кузнецова", "age": 19, "sex": "female",
              "email": "anna.kuznetsova@example.com"},
             {"id": 6, "name": "Сергей", "surname": "Попов", "age": 35, "sex": "male",
              "email": "sergey.popov@example.com"},
             {"id": 7, "name": "Ольга", "surname": "Васильева", "age": 22, "sex": "female",
              "email": "olga.vasilyeva@example.com"},
             {"id": 8, "name": "Андрей", "surname": "Соколов", "age": 50, "sex": "male",
              "email": "andrey.sokolov@example.com"},
             {"id": 9, "name": "Елена", "surname": "Михайлова", "age": 38, "sex": "female",
              "email": "elena.mihaylova@example.com"},
             {"id": 10, "name": "Alex%#", "surname": "Новиков", "age": 29, "sex": "male",
              "email": "alexey.novikov@example.com"}
             ]

    for user in users:
        user["is_alphanumeric"] = is_alphanumeric(user["name"])
        if user["is_alphanumeric"]:
            print(user)

    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={"data": users, "is_alphanumeric": is_alphanumeric}
    )
