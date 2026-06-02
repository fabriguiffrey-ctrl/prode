from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from app.database import Base


class Match(Base):
    __tablename__ = "matches"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    home_team = Column(
        String,
        nullable=False
    )

    away_team = Column(
        String,
        nullable=False
    )

    match_date = Column(
        DateTime,
        nullable=False
    )

    home_score = Column(
        Integer,
        default=0
    )

    away_score = Column(
        Integer,
        default=0
    )

    finished = Column(
        Boolean,
        default=False
    )