from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status

from datetime import datetime, timedelta
from jose import JWTError, jwt

from sqlalchemy import select

from ..models.Users import UsersModel
from ..schemas.data_models import UserHash, TokenData, UserModel, User

from ..config.tokens import SECRET_KEY, ALGORITHM
from ..config.db import get_db

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')


def verify_password(password: str, hashed_password: str):
    return pwd_context.verify(password, hashed_password)


def get_password_hash(password: str):
    return pwd_context.hash(password)


def get_user(username: str, db):
    selection = select(UsersModel).where(UsersModel.name == username).limit(1)
    user = db.execute(selection).scalar()
    if user is not None:
        res = UserModel.model_validate(user)
        return res


def authenticate_user(username: str, password: str, db):
    user = get_user(username, db)
    if not user:
        print('User not found')
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_token(data: dict, expires_delta: timedelta or None=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now()+expires_delta
    else:
        expire = datetime.now()+timedelta(minutes=15)

    to_encode.update({'exp': expire})
    encoded_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_token


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail='Server could not validate credentials',
                                         headers={'WWW-Authenticate': 'Bearer'})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if not username:
            raise credential_exception
        token_data = TokenData(name=username)
    except JWTError:
        raise credential_exception

    gen = get_db()
    db = next(gen)
    user = User.model_validate(get_user(token_data.name, db))
    if not user:
        raise credential_exception
    else:
        return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Inactive user',
                            headers={'WWW-Authenticate': 'Bearer'})
    else:
        return current_user
