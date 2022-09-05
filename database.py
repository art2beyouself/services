import sqlalchemy as db

from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URL = "postgresql://sme:thispasswordtoostrong@3.124.15.169:5432/smedb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
connection = engine.connect()
metadata = db.MetaData()
suppliers = db.Table('suppliers', metadata, autoload=True, autoload_with=engine)