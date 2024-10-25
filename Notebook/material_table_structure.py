# coding: utf-8
from sqlalchemy import BigInteger, Column, MetaData, Table, Text

metadata = MetaData()


t_material = Table(
    'material', metadata,
    Column('level_0', BigInteger, index=True),
    Column('index', BigInteger),
    Column('area', Text),
    Column('is_load_bearing', BigInteger),
    Column('matrtial', Text)
)
