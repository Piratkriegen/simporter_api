from datetime import date
from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel

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
    startDate: date
    endDate: date
    Type: Type
    Grouping: Grouping
    attr1: List[Filter]
    attr2: Optional[List[Filter]]

    class Config:
        orm_mode = True


class Date(str):
    date = "date"

class Values(int):
    values = List[int]

class Response(BaseModel):
    timeline: Dict[Date, Values]
