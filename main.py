from fastapi import FastAPI
from database import connection, db, metadata, engine


app = FastAPI()


suppliers = db.Table('suppliers', metadata, autoload=True, autoload_with=engine)
#Equivalent to 'SELECT * FROM census'
query = db.select([suppliers])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()


@app.get("/")
async def root():
    return(ResultSet)
