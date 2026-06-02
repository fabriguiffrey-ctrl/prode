from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.match import Match

from app.schemas.match import (
    MatchCreate,
    MatchResponse
)

router = APIRouter()

@router.post(
    "/matches",
    response_model=MatchResponse
)
def create_match(
    match: MatchCreate,
    db: Session = Depends(get_db)
):

    new_match = Match(
        home_team=match.home_team,
        away_team=match.away_team,
        match_date=match.match_date
    )

    db.add(new_match)

    db.commit()

    db.refresh(new_match)

    return new_match

@router.get(
    "/matches",
    response_model=list[MatchResponse]
)
def get_matches(
    db: Session = Depends(get_db)
):

    return db.query(Match).all()