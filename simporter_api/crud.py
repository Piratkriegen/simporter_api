from datetime import date
from sqlalchemy.orm import Session

from . import models, schemas


def get_events(db: Session, startDate: date, endDate: date, filters: dict):
    db_item = db.query(models.Event).\
        filter(models.Event.timestamp.between(startDate, endDate),\
            models.Event(**filters)).all()
    return db_item
