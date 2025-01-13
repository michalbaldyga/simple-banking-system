class Client:
    """
    A class used to represent a Client.

    Attributes
    ----------
    name : str
        the name of the client
    _balance : float
        the client's current balance

    Methods
    -------
    balance()
        Returns the current balance of the client.
    deposit(amount: float) -> None
        Adds the specified amount to the client's balance.
    withdraw(amount: float) -> None
        Subtracts the specified amount from the client's balance.
    """

    def __init__(
            self,
            name: str,
            balance: float
    ) -> None:
        """
        Parameters
        ----------
        name : str
            The name of the client.
        balance : float
            The initial balance of the client.
        """
        self.name = name
        self._balance = balance

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
