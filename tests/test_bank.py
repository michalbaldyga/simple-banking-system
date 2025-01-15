import pytest

from src.bank import Bank
from src.client import Client


@pytest.fixture
def client():
    return Client(client_id=1, name="Adam", balance=100.0)

@pytest.fixture
def bank():
    return Bank()

def test_add_client_valid(client, bank):
    bank.add_client(client)
    assert bank.clients[0] == client

def test_add_client_invalid(bank):
    with pytest.raises(TypeError, match="Only Client objects can be added."):
        bank.add_client(1)

def test_remove_client_valid(client, bank):
    bank.add_client(client)
    bank.remove_client(client_id=1)
    assert len(bank.clients) == 0

def test_remove_client_invalid(client, bank):
    with pytest.raises(ValueError, match="No client found with id 1."):
        bank.remove_client(client_id=1)
