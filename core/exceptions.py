class DomainError(Exception):
    """Base exception for all core e-commerce business rule violations."""
    pass

class OutOfStockError(DomainError):
    """Raised when a product does not have enough inventory to fulfill an order."""
    def __init__(self, product_name: str, requested: int, available: int):
        super().__init__(
            f"Insufficient stock for '{product_name}'. Requested: {requested}, Available: {available}."
        )

class InvalidOrderError(DomainError):
    """Raised when an order format is fundamentally broken (e.g., empty cart)."""
    pass

class UnauthorizedActionError(DomainError):
    """Raised when a user attempts an action restricted from their specific system role."""
    pass

class PaymentError(DomainError):
    """Base exception for all payment-related processing failures."""
    pass

class CardDeclinedError(PaymentError):
    """Raised when a mock transaction is explicitly refused by the processing engine."""
    pass