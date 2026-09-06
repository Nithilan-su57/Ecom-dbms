import random
from core.models import PaymentGatewayPayload
from core.exceptions import CardDeclinedError, InvalidOrderError

class MockPaymentService:
    @staticmethod
    def process_mock_payment(payload: PaymentGatewayPayload) -> str:
        """
        Processes a simulated card transaction.
        Returns a mock transaction reference string if successful, 
        or raises clear domain exceptions if validation conditions fail.
        """
        # 1. Structural Validation Rule Check
        if len(payload.card_number.replace(" ", "")) != 16:
            raise InvalidOrderError("Invalid card structure layout: Must be exactly 16 digits.")
            
        if len(payload.cvv) != 3:
            raise InvalidOrderError("Invalid security verification layout: CVV must be 3 digits.")

        # 2. Programmatic Sandbox Failures for Testing
        # Rule A: If card ends in '0000', simulate a hard bank decline
        if payload.card_number.endswith("0000"):
            raise CardDeclinedError("Transaction Refused: Insufficient funds in mock account.")
            
        # Rule B: If card ends in '9999', simulate a stolen card/security freeze
        if payload.card_number.endswith("9999"):
            raise CardDeclinedError("Transaction Refused: Mock payment flagged as fraudulent card status.")

        # 3. Standard Random Success Execution
        # 90% chance of success to mimic production network operations reliably
        if random.random() < 0.10:
            raise CardDeclinedError("Gateway Timeout: Unable to route simulated financial network request.")

        # Generate a distinct mock transaction token to store later in PostgreSQL
        mock_tx_ref = f"TXN_MOCK_{random.randint(10000000, 99999999)}"
        return mock_tx_ref