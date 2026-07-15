from typing import List
from core.models import Order, OrderItem, Product, User
from core.exceptions import OutOfStockError, InvalidOrderError, UnauthorizedActionError

class OrderService:
    @staticmethod
    def calculate_and_verify_checkout(
        user: User, 
        products_list: List[Product], 
        requested_quantities: List[int]
    ) -> Order:
        """
        Validates an incoming cart request against structural business metrics.
        Calculates totals and returns a fully priced transient Order model state.
        """
        # 1. Enforce Role Isolation
        if user.role != "customer":
            raise UnauthorizedActionError("Only verified customer accounts can initiate checkouts.")

        # 2. Structural Sanity Checks
        if not products_list or len(products_list) != len(requested_quantities):
            raise InvalidOrderError("Mismatched or empty cart inventory items provided.")

        order_items: List[OrderItem] = []
        running_total = 0.0

        # 3. Process each item mathematically
        for product, qty in zip(products_list, requested_quantities):
            if qty <= 0:
                raise InvalidOrderError(f"Quantities must be greater than zero. Got {qty} for {product.name}.")
                
            # Enforce stock checks in pure memory
            if product.stock_quantity < qty:
                raise OutOfStockError(
                    product_name=product.name, 
                    requested=qty, 
                    available=product.stock_quantity
                )

            # Deduct stock safely (Simulated transition state)
            product.stock_quantity -= qty

            # Compute line total
            line_cost = product.price * qty
            running_total += line_cost

            # Generate item record
            order_items.append(
                OrderItem(
                    product_id=product.product_id,
                    quantity=qty,
                    price_at_purchase=product.price
                )
            )

        # 4. Synthesize structural transient Order object
        return Order(
            order_id=None,  # Database engine will assign this sequence later
            user_id=user.user_id,
            items=order_items,
            total_amount=round(running_total, 2),
            status="pending"
        )