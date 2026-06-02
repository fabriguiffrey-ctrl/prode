from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.user import User
from app.models.match import Match

from app.routes.user_routes import router as user_router

from app.models.prediction import Prediction


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(user_router)

@app.get("/")
def root():
    return {
        "message": "Prode API funcionando"
    }

from app.routes.auth_routes import router as auth_router

app.include_router(auth_router)

from app.routes.match_routes import (
    router as match_router
)

app.include_router(match_router)

from app.routes.prediction_routes import (
    router as prediction_router
)

app.include_router(prediction_router)
