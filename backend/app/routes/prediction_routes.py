from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.prediction import Prediction

from app.schemas.prediction import (
    PredictionCreate,
    PredictionResponse
)

router = APIRouter()

@router.post(
    "/predictions",
    response_model=PredictionResponse
)
def create_prediction(
    prediction: PredictionCreate,
    db: Session = Depends(get_db)
):

    new_prediction = Prediction(
        user_id=prediction.user_id,
        match_id=prediction.match_id,
        prediction=prediction.prediction
    )

    db.add(new_prediction)

    db.commit()

    db.refresh(new_prediction)

    return new_prediction

@router.get(
    "/predictions",
    response_model=list[PredictionResponse]
)
def get_predictions(
    db: Session = Depends(get_db)
):

    return db.query(Prediction).all()