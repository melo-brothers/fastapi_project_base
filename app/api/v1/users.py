from app.models import Users
from fastapi import APIRouter

router = APIRouter()

@router.get("/user/")
def create_user():
    user = Users()
    return "ok", 200
