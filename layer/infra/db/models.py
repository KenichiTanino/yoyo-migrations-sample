import datetime
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import INET, TEXT
from sqlalchemy.ext.declarative import declarative_base


from .db import engine

Base = declarative_base()


class Addr(Base):
    __tablename__ = 'addr'
    id = Column(Integer, primary_key=True)
    name = Column(TEXT, nullable=True)
    addr = Column(TEXT, nullable=True)
    ipaddr = Column(INET, index=True, nullable=True)
    create_time = Column(DateTime, default=datetime.datetime.now)
    update_time = Column(DateTime, default=datetime.datetime.now)


Base.metadata.create_all(engine)
