from pydantic import BaseModel, ConfigDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str or None = None


class User(BaseModel):
    name: str
    disabled: bool or None = None

    model_config = ConfigDict(from_attributes=True)


class UserModel(BaseModel):
    id: int
    name: str
    disabled: bool
    password: str

    model_config = ConfigDict(from_attributes=True)

