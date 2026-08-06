from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from core.models import Base


engine = create_engine(
    "sqlite:///data/music.db"
)


Session = sessionmaker(
    bind=engine
)


def init_database():

    Base.metadata.create_all(
        engine
    )
