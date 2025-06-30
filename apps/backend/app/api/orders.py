from fastapi import APIRouter, Depends, HTTPException, Request
from app.middleware.auth import auth_required
from typing import Dict, Any, List
from pydantic import BaseModel
from datetime import datetime
from enum import Enum

router = APIRouter(prefix="/orders", tags=["orders"])


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    PREPARING = "preparing"
    READY = "ready"
    DELIVERED = "delivered"
    CANCELLED = "cancelled"


class OrderItem(BaseModel):
    menu_item_id: str
    quantity: int
    notes: str | None = None


class CreateOrderRequest(BaseModel):
    items: List[OrderItem]
    delivery_address: str | None = None
    is_takeaway: bool = False
    notes: str | None = None


class Order(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total: float
    status: OrderStatus
    created_at: datetime
    updated_at: datetime
    delivery_address: str | None = None
    is_takeaway: bool = False
    notes: str | None = None


# Mock data
ORDERS = []


@router.get("/", response_model=List[Order])
async def get_user_orders(
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Get all orders for the authenticated user"""
    user_id = request.state.user["id"]
    user_orders = [order for order in ORDERS if order["user_id"] == user_id]
    return user_orders


@router.get("/{order_id}", response_model=Order)
async def get_order(
    order_id: str,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Get a specific order (only if it belongs to the user)"""
    user_id = request.state.user["id"]
    
    for order in ORDERS:
        if order["id"] == order_id:
            if order["user_id"] != user_id:
                raise HTTPException(status_code=403, detail="Not authorized to view this order")
            return order
    
    raise HTTPException(status_code=404, detail="Order not found")


@router.post("/", response_model=Order)
async def create_order(
    order_request: CreateOrderRequest,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Create a new order"""
    user_id = request.state.user["id"]
    
    # Calculate total (mock calculation)
    total = sum(item.quantity * 10.0 for item in order_request.items)  # Mock price
    
    new_order = {
        "id": str(len(ORDERS) + 1),
        "user_id": user_id,
        "items": [item.dict() for item in order_request.items],
        "total": total,
        "status": OrderStatus.PENDING,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        "delivery_address": order_request.delivery_address,
        "is_takeaway": order_request.is_takeaway,
        "notes": order_request.notes
    }
    
    ORDERS.append(new_order)
    return new_order


@router.post("/{order_id}/cancel")
async def cancel_order(
    order_id: str,
    request: Request,
    token_payload: Dict[str, Any] = Depends(auth_required)
):
    """Cancel an order (only if it belongs to the user and is cancellable)"""
    user_id = request.state.user["id"]
    
    for order in ORDERS:
        if order["id"] == order_id:
            if order["user_id"] != user_id:
                raise HTTPException(status_code=403, detail="Not authorized to cancel this order")
            
            if order["status"] not in [OrderStatus.PENDING, OrderStatus.CONFIRMED]:
                raise HTTPException(status_code=400, detail="Order cannot be cancelled")
            
            order["status"] = OrderStatus.CANCELLED
            order["updated_at"] = datetime.now()
            return {"message": "Order cancelled successfully"}
    
    raise HTTPException(status_code=404, detail="Order not found")