from sqlalchemy.orm import Session
import models, schemas
from geopy.distance import geodesic

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

def get_address(db: Session, address_id: int):  # Get address
    return db.query(models.Address).filter(models.Address.id == address_id).first()

def delete_address(db: Session, address_id: int):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    
    if address:
        db.delete(address)
        db.commit()
    
    return address

def update_address(db: Session, address_id: int, updated: schemas.AddressUpdate):
    address = db.query(models.Address).filter(models.Address.id == address_id).first()
    
    if address:
        address.name = updated.name
        address.latitude = updated.latitude
        address.longitude = updated.longitude

        db.commit()
        db.refresh(address)

    return address

def get_nearby_addresses(db: Session, lat: float, lng: float, distance_km: float):
    addresses = db.query(models.Address).all()
    
    result = []

    for addr in addresses:
        addr_coords = (addr.latitude, addr.longitude)
        input_coords = (lat, lng)

        dist = geodesic(input_coords, addr_coords).km

        if dist <= distance_km:
            result.append(addr)

    return result