from src.transaction import Transaction, TransactionType


class Client:
    """
    A class used to represent a Client.

    Attributes
    ----------
    client_id : int
        the unique id of the client
    name : str
        the name of the client
    _balance : float
        the client's current balance
    transactions : list[Transaction]

    Methods
    -------
    balance() -> float
        Returns the current balance of the client.
    deposit(amount: float) -> None
        Adds the specified amount to the client's balance.
    withdraw(amount: float) -> None
        Subtracts the specified amount from the client's balance.
    _register_transaction(transaction_type: str, amount: float) -> None
        Registers a transaction whenever a deposit or withdrawal is made.
    print_statement() -> None
        Prints the statement of the client's transaction history.
    """

    def __init__(
            self,
            client_id: int,
            name: str,
            balance: float
    ) -> None:
        """
        Parameters
        ----------
        client_id : int
            The unique id of the client.
        name : str
            The name of the client.
        balance : float
            The initial balance of the client.
        """
        self.client_id = client_id
        self.name = name
        self._balance = balance
        self.transactions = []

    def __repr__(self):
        return (
            f"{self.__class__.__qualname__}(client_id={self.client_id!r}, "
            f"name={self.name!r}, "
            f"balance={self.balance!r})"
        )

    def __str__(self):
        return (
            f"Client ID={self.client_id}, "
            f"Name={self.name}, "
            f"Balance=${self.balance:.2f}"
        )

    @property
    def balance(self) -> float:
        """Gets the current balance of the client.

        Returns
        -------
        float
            The current balance of the client's account.
        """
        return self._balance

    def deposit(
            self,
            amount: float
    ) -> None:
        """Adds the specified amount to the client's balance.

        Parameters
        ----------
        amount : float
            The amount to be added to the client's balance.

        Raises
        ------
        ValueError
            If the deposit amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        self._register_transaction(TransactionType.DEPOSIT, amount)

    def withdraw(
            self,
            amount: float
    ) -> None:
        """Subtracts the specified amount from the client's balance.

        Parameters
        ----------
        amount : float
            The amount to be subtracted from the client's balance.

        Raises
        ------
        ValueError
            If the withdrawal amount is less than or equal to zero.
        ValueError
            If the withdrawal amount exceeds available balance.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Withdrawal amount exceeds available balance.")
        self._balance -= amount
        self._register_transaction(TransactionType.WITHDRAW, amount)

    def _register_transaction(
            self,
            transaction_type: TransactionType,
            amount: float
    ) -> None:
        """Registers a transaction whenever a deposit or withdrawal is made.

        Parameters
        ----------
        transaction_type : TransactionType
            The type of transaction (withdraw/deposit).
        amount : float
            The amount of transaction.
        """
        transaction = Transaction(self.name, transaction_type, amount)
        self.transactions.append(transaction)

    def print_statement(
            self
    ) -> None:
        """Prints the statement of the client's transaction history."""
        if not self.transactions:
            print(f"{self.name} has no transaction history.")
        else:
            print(f"{self.name} transaction history:")
            for transaction in self.transactions:
                print(transaction)
