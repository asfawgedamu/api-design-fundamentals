from fastapi import APIRouter

from app.services.menu_service import get_all_menu_items

router = APIRouter()

@router.get("/menu")

def get_menu():

    return get_all_menu_items()