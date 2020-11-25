import datetime
from sqlalchemy.orm import Session
from . import models
from . import schemas


import logging
logger = logging.getLogger(__name__)


def get_addrs(db: Session):
    return db.query(models.Addr).all()


def get_addr_by_id(db: Session, id: int):
    return db.query(models.Addr).filter(models.Addr.id == id).first()


def create_addr_query(db: Session, addr: schemas.AddrCreateEntity):
    db_addr = models.Addr(name=addr.name,
                          addr=addr.addr,
                          ipaddr=addr.ipaddr,
                          create_time=datetime.datetime.now())
    db.add(db_addr)
    db.commit()
    db.refresh(db_addr)
    return db_addr


from collections import OrderedDict


def asdict(self):
    result = OrderedDict()
    for key in self.__mapper__.c.keys():
        if getattr(self, key) is not None:
            result[key] = str(getattr(self, key))
        else:
            result[key] = getattr(self, key)
    return result


def update_addr_query(db: Session, addr: schemas.AddrUpdateEntity):
    db_addr = db.query(models.Addr).filter(models.Addr.id==addr.id).first()

    db_addr.name = addr.name
    db_addr.addr = addr.addr
    db_addr.ipaddr = addr.ipaddr
    db_addr.update_time = datetime.datetime.now()

    db.commit()
    # 辞書に変更しないと、modelsがそのまま反映されてしまうため
    asdict(db_addr)
    return db_addr


def delete_addr_query(db: Session, addr: schemas.AddrUpdateEntity):
    db_addr = db.query(models.Addr).filter(models.Addr.id==addr.id).first()
    db.delete(db_addr)
    db.commit()
    return
