from datetime import datetime

class Transaction:
    """
    A class used to represent a Transaction.

    Attributes
    ----------
    client_name : int
        the name of the client who made the transaction
    transaction_type : str
        the type of transaction (withdraw/deposit)
    transaction_amount : float
        the amount of transaction
    transaction_date : datetime
        the transaction date
    """

    def __init__(
            self,
            client_name: str,
            transaction_type: str,
            transaction_amount: float
    ) -> None:
        """
        Initializes transaction.

        Parameters
        ----------
        client_name : str
            The name of the client who made the transaction.
        transaction_type : str
            The type of transaction (withdraw/deposit)
        transaction_amount : float
            The amount of the transaction.
        """
        self.client_name = client_name
        self.transaction_type = transaction_type
        self.transaction_amount = transaction_amount
        self.transaction_date = datetime.now()

    def __repr__(self):
        return (
            f"Transaction("
            f"client_name='{self.client_name}', "
            f"transaction_type='{self.transaction_type}', "
            f"transaction_amount={self.transaction_amount}, "
            f"transaction_date='{self.transaction_date}')"
        )

    def __str__(self):
        return (
            f"Transaction: "
            f"Type={self.transaction_type}, "
            f"Amount=${self.transaction_amount:.2f}, "
            f"Date={self.transaction_date.strftime('%Y-%m-%d %H:%M:%S')}"
        )
