from pydantic import BaseModel


class Data(BaseModel):
    login: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str or None = None


class User(BaseModel):
    username: str
    expired: bool or None=None


class UserHash(User):
    hashed_password: str

