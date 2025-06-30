from fastapi import APIRouter, Depends, HTTPException, Request
from app.middleware.auth import auth_required, optional_auth
from typing import Dict, Any, List
from pydantic import BaseModel

router = APIRouter(prefix="/menu", tags=["menu"])


# Pydantic models
class MenuItem(BaseModel):
    id: str
    name: str
    description: str
    price: float
    category: str
    available: bool = True
    image_url: str | None = None


class MenuCategory(BaseModel):
    id: str
    name: str
    description: str | None = None
    display_order: int = 0


# Mock data for now
MENU_ITEMS = [
    {
        "id": "1",
        "name": "Margherita Pizza",
        "description": "Fresh tomatoes, mozzarella, basil",
        "price": 12.99,
        "category": "pizza",
        "available": True
    },
    {
        "id": "2",
        "name": "Caesar Salad",
        "description": "Romaine lettuce, parmesan, croutons, caesar dressing",
        "price": 8.99,
        "category": "salads",
        "available": True
    }
]

CATEGORIES = [
    {"id": "pizza", "name": "Pizza", "display_order": 1},
    {"id": "salads", "name": "Salads", "display_order": 2},
    {"id": "desserts", "name": "Desserts", "display_order": 3}
]


@router.get("/items", response_model=List[MenuItem])
async def get_menu_items(
    category: str | None = None,
    available_only: bool = True,
    token_payload: Dict[str, Any] = Depends(optional_auth)
):
    """Get all menu items (public endpoint)"""
    items = MENU_ITEMS
    
    if category:
        items = [item for item in items if item["category"] == category]
    
    if available_only:
        items = [item for item in items if item["available"]]
    
    return items


@router.get("/items/{item_id}", response_model=MenuItem)
async def get_menu_item(item_id: str):
    """Get a specific menu item (public endpoint)"""
    for item in MENU_ITEMS:
        if item["id"] == item_id:
            return item
    
    raise HTTPException(status_code=404, detail="Menu item not found")


@router.get("/categories", response_model=List[MenuCategory])
async def get_categories():
    """Get all menu categories (public endpoint)"""
    return sorted(CATEGORIES, key=lambda x: x["display_order"])


# Admin endpoints (require authentication)
@router.post("/items", response_model=MenuItem)
async def create_menu_item(
    item: MenuItem,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Create a new menu item (admin only)"""
    # TODO: Check if user is admin
    # For now, just check if authenticated
    
    # Add to mock data
    new_item = item.dict()
    new_item["id"] = str(len(MENU_ITEMS) + 1)
    MENU_ITEMS.append(new_item)
    
    return new_item


@router.put("/items/{item_id}", response_model=MenuItem)
async def update_menu_item(
    item_id: str,
    item: MenuItem,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Update a menu item (admin only)"""
    # TODO: Check if user is admin
    
    for idx, existing_item in enumerate(MENU_ITEMS):
        if existing_item["id"] == item_id:
            updated_item = item.dict()
            updated_item["id"] = item_id
            MENU_ITEMS[idx] = updated_item
            return updated_item
    
    raise HTTPException(status_code=404, detail="Menu item not found")


@router.delete("/items/{item_id}")
async def delete_menu_item(
    item_id: str,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Delete a menu item (admin only)"""
    # TODO: Check if user is admin
    
    for idx, item in enumerate(MENU_ITEMS):
        if item["id"] == item_id:
            MENU_ITEMS.pop(idx)
            return {"message": "Menu item deleted"}
    
    raise HTTPException(status_code=404, detail="Menu item not found")