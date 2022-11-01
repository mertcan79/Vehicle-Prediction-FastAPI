from pydantic import BaseModel, conlist
from typing import List, Any


class Vehicle(BaseModel):
    data: List[Any]


class VehiclePredictionResponse(BaseModel):
    prediction: int
