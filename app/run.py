
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from starlette.requests import Request
import sys
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db 

# import logging
# logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from app.urls import router as app_router
from app.settings.settings import Settings

origins = [
    "http://192.168.132.128:18000",
    "http://192.168.0.12:18000",
]

settings = Settings()

app = FastAPI(openapi_url='/openapi.json')
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(app_router)
