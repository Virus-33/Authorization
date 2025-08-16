from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    username: str
    disabled: bool or None = None


class UserHash(User):
    hashed_password: str


class UserModel(BaseModel):
    id: int
    name: str
    disabled: bool
    password: str

