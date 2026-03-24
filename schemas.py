from pydantic import BaseModel          #For validation

class AddressCreate(BaseModel):
    name: str
    latitude: float
    longitude: float