class Client:

    def __init__(
            self,
            name: str,
            balance: float
    ) -> None:
        self.name = name
        self._balance = balance

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(
            self,
            amount: float
    ) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount

    def withdraw(
            self,
            amount: float
    ) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self._balance:
            raise ValueError("Withdrawal amount exceeds available balance.")
        self._balance -= amount
