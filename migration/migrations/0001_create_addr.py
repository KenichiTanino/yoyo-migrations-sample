#
# file: migrations/0001_create_foo.py
#
from yoyo import step

steps = [
  step("create table addr (id SERIAL, name text, addr text, ipaddr inet, create_time timestamp with time zone, update_time timestamp with time zone);"),
]
