from datetime import date, datetime
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, validator

import time

class Type(str, Enum):
    cumulative = "cumulative"
    usual = "usual"

class Grouping(str, Enum):
    weekly = "weekly"
    biweekly = "bi-weekly"
    monthly = "monthly"

class Filter(str):
    asin = "asin"
    brand = "brand"
    id = "id"
    source = "source"
    stars = "stars"
    timestamp = "timestamp"

class Event(BaseModel):
    startDate: int
    endDate: int
    Type: Type
    Grouping: Grouping
    attr1: List[Filter]
    attr2: Optional[List[Filter]]

    @validator('startDate', pre=True)
    def convert_startDate(cls, v):
        return time.mktime(
            datetime.strptime(v, "%Y-%m-%d").timetuple())

    @validator('endDate', pre=True)
    def convert_endDate(cls, v):
        return time.mktime(
            datetime.strptime(v, "%Y-%m-%d").timetuple())

    class Config:
        orm_mode = True


class Date(str):
    date = "date"

class Values(int):
    values = List[int]

class Response(BaseModel):
    timeline: Dict[Date, Values]
