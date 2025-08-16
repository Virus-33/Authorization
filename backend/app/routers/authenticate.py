from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends)
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

from ..config.db import get_db, SessionLocal
from ..config.tokens import TOKEN_EXPIRATION_HOURS

from ..schemas import Token, User

from ..security_logic import user_authentication

router =APIRouter(
    tags=['auth']
)


@router.post('/token', response_model=Token)
async def login_by_token(form_data: OAuth2PasswordRequestForm = Depends(), db: SessionLocal = Depends(get_db)):
    user = user_authentication.authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Incorrect username or data',
                            headers={'WWW-Authenticate': 'Bearer'})
    token_expires_delta = timedelta(hours=int(TOKEN_EXPIRATION_HOURS))
    token = user_authentication.create_token(data={'sub': user.name}, expires_delta=token_expires_delta)
    return {'access_token': token, 'token_type': 'bearer'}


@router.get('/users/me', response_model=User)
async def read_current_user(current_user: User = Depends(user_authentication.get_current_active_user)):
    return current_user

