import sqlalchemy as db

from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = ""
engine = create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.connect()
metadata = db.MetaData()
suppliers = db.Table('suppliers_stage', metadata, autoload=True, autoload_with=engine)
