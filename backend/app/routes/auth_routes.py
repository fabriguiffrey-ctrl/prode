from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.models.user import User

from app.schemas.auth import (
    LoginRequest,
    TokenResponse
)

from app.auth.security import (
    verify_password,
    create_access_token
)

router = APIRouter()

@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    credentials: LoginRequest,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(
            User.email ==
            credentials.email
        )
        .first()
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    valid_password = verify_password(
        credentials.password,
        user.password_hash
    )

    if not valid_password:

        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    token = create_access_token(
        {
            "sub": str(user.id)
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }