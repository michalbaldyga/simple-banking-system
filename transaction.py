from datetime import datetime

class Transaction:

    def __init__(
            self,
            client_name: str,
            transaction_type: str,
            transaction_amount: float
    ) -> None:
        self.client_name = client_name
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = datetime.now()
