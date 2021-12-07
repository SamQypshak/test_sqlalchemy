from sqlalchemy import Column, String, Float

from database import Base


class Partner(Base):
    __tablename__ = 'partners'
    id=Column(String,primary_key=True)
    code=Column('code', String(32))
    name=Column('name', String)

class Debts(Base):
    __tablename__ = 'debts'
    id = Column(String, primary_key=True)
    partner_id = Column('partner_id', String(50))
    sum = Column('sum', Float)

class Products(Base):
    __tablename__ = 'products'
    id = Column(String, primary_key=True)
    name = Column('name', String(100))
    parent_id = Column('parent_id', String(100))