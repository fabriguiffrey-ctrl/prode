from pydantic import BaseModel
from datetime import datetime


class PredictionCreate(BaseModel):

    user_id: int

    match_id: int

    prediction: str


class PredictionResponse(BaseModel):

    id: int

    user_id: int

    match_id: int

    prediction: str

    created_at: datetime

    class Config:
        from_attributes = True