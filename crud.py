from sqlalchemy.orm import Session
import models, schemas

def create_address(db: Session, address: schemas.AddressCreate):
    db_address = models.Address(
        name=address.name,
        latitude=address.latitude,
        longitude=address.longitude
    )
    db.add(db_address)
    db.commit()
    db.refresh(db_address)
    return db_address

def get_addresses(db: Session):
    return db.query(models.Address).all()