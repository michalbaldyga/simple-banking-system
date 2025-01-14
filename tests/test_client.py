import pytest
from src.client import Client


@pytest.fixture
def client():
    return Client(client_id=1, name="Adam", balance=100.0)


def test_deposit_valid(client):
    client.deposit(50.0)
    assert client.balance == 150.0


