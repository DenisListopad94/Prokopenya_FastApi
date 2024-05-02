from src.book_app.models import Booking
from src.core.models import Base
from src.auth.enum import UserRole
from sqlalchemy.orm import Mapped, mapped_column, relationship
from src.core.models.base import (
    str_30,
    created_at,
    updated_at
)


class User(Base):
    f_name: Mapped[str_30]
    l_name: Mapped[str_30]
    role: Mapped[UserRole] = mapped_column(default=UserRole.user.value)
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
    booking: Mapped[list["Booking"]] = relationship("Booking", back_populates="user")
