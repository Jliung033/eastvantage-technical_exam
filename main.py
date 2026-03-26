from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# dependency (get DB session)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"Hello": "World"}

# CREATE address
@app.post("/addresses")
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)

# GET ALL addresses
@app.get("/addresses")
def get_addresses(db: Session = Depends(get_db)):
    return crud.get_addresses(db)

# NEARBY search
@app.get("/addresses/nearby")
def get_nearby_addresses(
    lat: float,
    lng: float,
    distance_km: float,
    db: Session = Depends(get_db)
):
    return crud.get_nearby_addresses(db, lat, lng, distance_km)

# GET address by ID
@app.get("/addresses/{address_id}")
def get_address(address_id: int, db: Session = Depends(get_db)):
    address = crud.get_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

# UPDATE address
@app.put("/addresses/{address_id}")
def update_address(address_id: int, updated: schemas.AddressUpdate, db: Session = Depends(get_db)):
    address = crud.update_address(db, address_id, updated)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address


# DELETE address
@app.delete("/addresses/{address_id}")
def delete_address(address_id: int, db: Session = Depends(get_db)):
    address = crud.delete_address(db, address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address