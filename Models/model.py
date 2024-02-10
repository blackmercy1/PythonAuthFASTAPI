from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import Table, Column, MetaData, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column

metadata = MetaData()


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)
    jwt_access_token: dict = Field(default=None)
    jwt_refresh_token: dict = Field(default=None)

    class Config:
        from_attributes = True


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    login_schema: UserLoginSchema = Field(default=None)

    class Config:
        from_attributes = True


roles = Table(
    "user",
    metadata,
    Column("Id", Integer, primary_key=True, index=True),
    Column("email", String, nullable=False, unique=True, index=True),
    Column("username", String),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)
