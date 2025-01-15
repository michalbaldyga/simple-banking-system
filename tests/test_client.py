import pytest

from src.client import Client
from src.transaction import TransactionType


@pytest.fixture
def client():
    return Client(client_id=1, name="Adam", balance=100.0)

def test_deposit_valid(client):
    client.deposit(50.0)
    assert client.balance == 150.0
    assert len(client.transactions) == 1
    assert client.transactions[0].transaction_type == TransactionType.DEPOSIT

def test_deposit_invalid(client):
    with pytest.raises(
        ValueError,
        match="Deposit amount must be greater than zero."
    ):
        client.deposit(-50.0)

def test_withdraw_valid(client):
    client.withdraw(50.0)
    assert client.balance == 50.0
    assert len(client.transactions) == 1
    assert client.transactions[0].transaction_type == TransactionType.WITHDRAW

def test_withdraw_negative_amount(client):
    with pytest.raises(
            ValueError,
            match="Withdrawal amount must be greater than zero."):
        client.withdraw(-50.0)

def test_withdraw_exceed_balance(client):
    with pytest.raises(
            ValueError,
            match="Withdrawal amount exceeds available balance."):
        client.withdraw(300.0)
