from pydantic import BaseModel, EmailStr, PositiveInt, Field, constr
from typing_extensions import Literal
from datetime import datetime
from typing import Optional

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)

from src.auth.enum import UserRole


class UserBaseSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole


class UserCreateSchema(UserBaseSchema):
    pass


class UserReadSchema(UserBaseSchema):
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class UserUpdatePartialSchema(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    role: UserRole | None = None


class UserUpdateSchema(BaseModel):
    first_name: str
    last_name: str
    role: UserRole


class UserCreateRetrieveSchema(UserBaseSchema):
    model_config = ConfigDict(from_attributes=True)
    id: int


class User(BaseModel):
    user_id: PositiveInt
    name: constr(min_length=2, max_length=20)
    surname: constr(min_length=2, max_length=20)
    age: int = Field(ge=0, le=100)
    sex: Literal["male", "female"]
    email: EmailStr
