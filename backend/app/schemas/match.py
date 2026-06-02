from pydantic import BaseModel
from datetime import datetime


class MatchCreate(BaseModel):
    home_team: str
    away_team: str
    match_date: datetime


class MatchResponse(BaseModel):
    id: int

    home_team: str
    away_team: str

    match_date: datetime

    home_score: int
    away_score: int

    finished: bool

    class Config:
        from_attributes = True