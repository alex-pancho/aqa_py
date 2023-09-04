from pydantic import BaseModel, Field, validator


class Data(BaseModel):
    user_id: int = Field(alias="userId", ge=1)
    distance_units: str = Field(alias="distanceUnits")
    currency: str


class Post(BaseModel):
    status: str
    data: Data

    @validator('status')
    def check_status(cls, value: str):
        if value != 'ok':
            raise ValueError("wrong status")
        return value


class Error(BaseModel):
    status: str
    message: str

    @validator('status')
    def check_status(cls, value: str):
        if value != 'error':
            raise ValueError("wrong status")
        return value


class Get(BaseModel):
    status: str


