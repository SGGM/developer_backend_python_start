from fastapi import FastAPI

from app.api import track_points
from app.db import engine, database, metadata


app = FastAPI()

metadata.create_all(engine)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(track_points.router, prefix="/api/v1")
