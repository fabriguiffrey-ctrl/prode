from fastapi import FastAPI

from app.database import Base
from app.database import engine

from app.models.user import User

from app.routes.user_routes import router as user_router

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