
from fastapi import FastAPI
import os
from starlette.requests import Request
import sys
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db 

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(ROOT_DIR)

from app.urls import router as app_router
from app.settings.settings import Settings


settings = Settings()

app = FastAPI(openapi_url='/openapi.json')
app.add_middleware(DBSessionMiddleware, db_url=settings.DATABASE_URI)


app.include_router(app_router)
