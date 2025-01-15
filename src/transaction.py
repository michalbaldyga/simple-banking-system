from datetime import datetime
from enum import StrEnum


class TransactionType(StrEnum):
    """Enum representing the types of transactions."""
    WITHDRAW = "withdraw"
    DEPOSIT = "deposit"


class Transaction:
    """
    A class used to represent a Transaction.

    Attributes
    ----------
    client_name : int
        the name of the client who made the transaction
    transaction_type : TransactionType
        the type of transaction (withdraw/deposit)
    transaction_amount : float
        the amount of transaction
    transaction_date : datetime
        the transaction date
    """

    def __init__(
            self,
            client_name: str,
            transaction_type: TransactionType,
            transaction_amount: float
    ) -> None:
        """
        Initializes transaction.

        Parameters
        ----------
        client_name : str
            The name of the client who made the transaction.
        transaction_type : TransactionType
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
            f"{self.__class__.__qualname__}("
            f"client_name={self.client_name!r}, "
            f"transaction_type={self.transaction_type!r}, "
            f"transaction_amount={self.transaction_amount!r}, "
            f"transaction_date={self.transaction_date!r})"
        )

    def __str__(self):
        return (
            r"Transaction: Type={}, Amount=${:.2f}, Date={}"
        ).format(
            self.transaction_type,
            self.transaction_amount,
            self.transaction_date.strftime('%Y-%m-%d %H:%M:%S')
        )
