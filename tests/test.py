import sys
import os

# Add the parent directory (root folder) to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now your imports will work flawlessly
from core.models import PaymentGatewayPayload
from core.services.payment_service import MockPaymentService
from core.exceptions import CardDeclinedError

# Test Case 1: Processing a standard valid payment
valid_card = PaymentGatewayPayload(
    card_holder_name="Alice Smith",
    card_number="1234 5678 1234 5678",
    expiry_date="12/29",
    cvv="123",
    amount=2400.00
)

try:
    tx_id = MockPaymentService.process_mock_payment(valid_card)
    print(f"Payment Authorized! Reference Token: {tx_id}")
except Exception as e:
    print(f"Payment failed: {e}")

# Test Case 2: Forcing a programmatic decline via our '0000' rule
declined_card = PaymentGatewayPayload(
    card_holder_name="Alice Smith",
    card_number="1234 5678 1234 0000", # Triggers rule A
    expiry_date="12/29",
    cvv="999",
    amount=2400.00
)

try:
    MockPaymentService.process_mock_payment(declined_card)
except CardDeclinedError as error:
    print(f"\nCaught Expected Rejection: {error}")



try:
    tx_id = MockPaymentService.process_mock_payment(valid_card)
  
    print(f"Payment Authorized! Reference Token: {tx_id}")
except Exception as e:
    print(f"Payment failed: {e}")