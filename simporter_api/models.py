from sqlite3 import Date
from sqlalchemy import Column, Integer, String, TIMESTAMP, TypeDecorator

from datetime import datetime
import time

from .database import Base


class DoubleTimestamp(TypeDecorator):

    def __init__(self):
        TypeDecorator.__init__(self, as_decimal=False)

    def process_bind_param(self, value, dialect):
        return datetime.utcfromtimestamp(value).strftime('%Y-%m-%d')

class Event(Base):
    __tablename__ = "data"

    asin = Column(String)
    brand = Column(String)
    id = Column(String, primary_key=True, index=True)
    source = Column(String)
    stars = Column(Integer)
    timestamp = Column(DoubleTimestamp)
