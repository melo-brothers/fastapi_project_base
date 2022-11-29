from app.api.v1 import observer, users
from app.database import DBSession
from fastapi import FastAPI

app = FastAPI()

app.include_router(observer.router)
app.include_router(users.router)


async def get_db():
    db = DBSession()
    try:
        yield db
    finally:
        db.close()