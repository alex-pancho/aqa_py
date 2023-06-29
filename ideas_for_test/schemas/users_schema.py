from pydantic import BaseModel, Field


class DataCurrent(BaseModel):
    user_id: int = Field(alias="userId", ge=1)
    distance_units: str = Field(alias="distanceUnits")
    currency: str
    photo_filename: str = Field(alias="photoFilename")


class DataProfile(BaseModel):
    user_id: int = Field(alias="userId", ge=1)
    photo_filename: str = Field(alias="photoFilename")
    name: str
    last_name: str = Field(alias="lastName")


class GetCurrent(BaseModel):
    status: str
    data: DataCurrent


class GetProfile(BaseModel):
    status: str
    data: DataProfile


class Error(BaseModel):
    status: str
    message: str
