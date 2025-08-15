from sqlalchemy import Integer, String, Boolean

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from ..config.db import Base


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    name: Mapped[String] = mapped_column(String(40), nullable=False)
    disabled: Mapped[Boolean] = mapped_column(Boolean, nullable=False)
