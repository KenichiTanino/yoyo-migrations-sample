from datetime import datetime
from pydantic import BaseModel


class Addr(BaseModel):
    id: int
    name: str
    addr: str
    ipaddr: str
    create_time: datetime
    update_time: datetime


class AddrCreateEntity(BaseModel):
    name: str
    addr: str
    ipaddr: str


class AddrUpdateEntity(BaseModel):
    id: int
    name: str
    addr: str
    ipaddr: str


class AddrDeleteEntity(BaseModel):
    id: int
