from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db import get_db, init_db
from app.models import Station

app = FastAPI()

@app.on_event("startup")
def startup():
    init_db()

class StationCreate(BaseModel):
    status: str = "open"
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    capacity: int = Field(ge=1)

class StationOut(BaseModel):
    id: int
    code: str
    name: str
    capacity: int
    status: str

class StationPatch(BaseModel):
    status: Optional[str] = None
    name: Optional[str] = None

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/stations")
def get_stations(status: str = None, db: Session = Depends(get_db)):
    if status is None:
        return db.query(Station).all()
    return db.query(Station).filter(Station.status == status).all()

@app.get("/stations/{station_id}", response_model=StationOut)
def get_station(station_id: int, db: Session = Depends(get_db)):
    station = db.get(Station, station_id)
    if station is None:
        raise HTTPException(status_code=404)
    return station

@app.post("/stations", response_model=StationOut, status_code=201)
def create_station(data: StationCreate, db: Session = Depends(get_db)):
    if data.status not in ["open", "closed", "maintenance"]:
        raise HTTPException(status_code=422)
    new_station = Station(
        code=data.code,
        name=data.name,
        capacity=data.capacity,
        status=data.status,
    )
    try:
        db.add(new_station)
        db.commit()
        db.refresh(new_station)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Code déjà utilisé")
    return new_station

@app.patch("/stations/{station_id}", response_model=StationOut)
def patch_station(station_id: int, data: StationPatch, db: Session = Depends(get_db)):
    station = db.get(Station, station_id)
    if station is None:
        raise HTTPException(status_code=404)
    if data.name is not None:
        station.name = data.name
    if data.status is not None:
        if data.status not in ["open", "closed", "maintenance"]:
            raise HTTPException(status_code=422)
        station.status = data.status
    db.commit()
    db.refresh(station)
    return station