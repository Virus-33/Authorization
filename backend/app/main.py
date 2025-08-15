from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer

from routers import authenticate

from pydantic import BaseModel

# from config.db import Base
# from config.db import engine


app = FastAPI(
    title='Simple authorization',
    docs_url='/docs',
    redoc_url=None
)

# app.mount('/static', StaticFiles(directory='app/statis'), name='static')

'''
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)
'''

# Base.metadata.create_all(bind=engine)

app.include_router(authenticate.router)
