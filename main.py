from fastapi import FastAPI, Depends
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

# create address
@app.post("/addresses")
def create_address(address: schemas.AddressCreate, db: Session = Depends(get_db)):
    return crud.create_address(db, address)