
from fastapi import APIRouter
from starlette.requests import Request
from sqlalchemy.orm import Session

from fastapi_sqlalchemy import db

from layer.infra.db.models import Addr
from layer.infra.db.schemas import Addr, AddrCreateEntity, AddrUpdateEntity, AddrDeleteEntity
from layer.infra.db.action import create_addr_query, update_addr_query, delete_addr_query, get_addrs, get_addr_by_id


router = APIRouter()


def get_success_result(result):
    return dict(StatusCode=200, ErrorCode='',Result=result)


@router.get("/addrs")
async def addrs_findall(request: Request):
    result = get_addrs(db.session)
    return get_success_result(result)


@router.get("/addrs/find/{id}")
async def addrs_findone(id: int):
    result = get_addr_by_id(db.session, id)
    return get_success_result(result)


@router.post("/addrs/create")
async def addrs_create(addr: AddrCreateEntity):
    result = create_addr_query(db.session, addr)
    return get_success_result(result)


@router.post("/addrs/update")
async def addrs_update(addr: AddrUpdateEntity):
    result = update_addr_query(db.session, addr)
    return get_success_result(result)


@router.post("/addrs/delete")
async def addrs_delete(addr: AddrDeleteEntity):
    result = delete_addr_query(db.session, addr)
    return get_success_result("delete success")
