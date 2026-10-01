from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal
from sqlalchemy.orm import Session
from fastapi import Depends
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
    status: str = None
    name: str = None

@app.get("/health")
def health_stats():
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
def CreateStation(data: StationCreate):
    global next_id
    if data.status not in ["open", "closed", "maintenance"]:
        raise HTTPException(status_code=422)

    NewStation = {
        "id": next_id,
        "code": data.code,
        "capacity": data.capacity,
        "name": data.name,
        "status": data.status,
        }

    stations.append(NewStation)
    next_id += 1

    return NewStation

@app.patch("/stations/{station_id}", response_model=StationOut)
def patch_station(station_id: int, data: StationPatch):
    "je sais pas la suite m3 shcool me livre pas son secret"