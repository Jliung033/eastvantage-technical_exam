from pydantic import BaseModel, Field, field_validator

# For Validations

class AddressBase(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        description="Name must not be empty"
    )
    latitude: float
    longitude: float

    @field_validator("latitude")
    def validate_latitude(cls, v):
        if v < -90 or v > 90:
            raise ValueError("Latitude must be between -90 and 90")
        return v

    @field_validator("longitude")
    def validate_longitude(cls, v):
        if v < -180 or v > 180:
            raise ValueError("Longitude must be between -180 and 180")
        return v


class AddressCreate(AddressBase):
    pass


class AddressUpdate(AddressBase):
    pass