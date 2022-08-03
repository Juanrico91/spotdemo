# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///sql_app/sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sp0+l1ghT@34.136.186.127:5432/spotlight_campaign_db "

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:sp0+l1ghT@34.136.186.127:5432/spotlight_campaign_db"
# SQLALCHEMY_DATABASE_URI = PostgresDsn.build(
#     scheme="spotlight_campaign_db",
#     user="postgres",
#     password="sp0+l1ghT",
#     host="34.136.186.127",
#     path=f"postgresql://postgres:sp0+l1ghT@34.136.186.127:5432/spotlight_campaign_db",
# )
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
try:
    db = SessionLocal()
    db.execute("SELECT 1")
except Exception as e:
    raise e