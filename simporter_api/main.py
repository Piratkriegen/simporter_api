from typing import List, Optional

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/api/{timeline}/")
def read_events(timeline, db: Session = Depends(get_db)):
    timeline = schemas.Event
    events = crud.get_events(db, timeline)  # response_model=schemas.Response
    return events

@app.get("/{items}/")
async def read_items(timeline):
    return timeline
