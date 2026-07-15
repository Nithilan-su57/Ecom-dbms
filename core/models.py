from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class User:
    user_id: Optional[int]
    name: str
    email: str
    password_hash: str
    role: str  # 'customer', 'manager', 'admin'
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class Product:
    product_id: Optional[int]
    category_id: Optional[int]
    name: str
    description: str
    price: float
    stock_quantity: int
    created_at: datetime = field(default_factory=datetime.now)

@dataclass
class OrderItem:
    product_id: int
    quantity: int
    price_at_purchase: float

@dataclass
class Order:
    order_id: Optional[int]
    user_id: int
    items: List[OrderItem]
    total_amount: float = 0.0
    status: str = "pending"  # 'pending', 'processing', 'completed', 'cancelled'
    created_at: datetime = field(default_factory=datetime.now)  