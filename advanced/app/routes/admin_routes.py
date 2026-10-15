from fastapi import APIRouter
from fastapi import Depends

from app.security.api_key import verify_api_key

router = APIRouter()

@router.get("/admin")

def admin_dashboard(
    api_key: str = Depends(verify_api_key)
):

    return {
        "message": "Welcome Admin"
    }