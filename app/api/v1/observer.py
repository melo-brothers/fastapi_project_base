from fastapi import APIRouter, status

router = APIRouter()


@router.get("/health/", tags=["health"], status_code=status.HTTP_200_OK)
async def health():
    return "UP!"
