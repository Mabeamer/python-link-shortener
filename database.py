#this all has to change for local db for extension project?

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import get_setttings


engine = crate_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocomit = False, autoflush = False, bind = engine

)

Base = declarative_base()

