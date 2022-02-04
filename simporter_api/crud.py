from sqlalchemy.orm import Session

from . import models, schemas


def get_events(db: Session, consult: schemas.Event):
    db_item = db.query(models.Event).\
        filter(models.Event.timestamp.between(consult.startDate, consult.endDate),\
            models.Event(consult.attr1)).all()
    return db_item
