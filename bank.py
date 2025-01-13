from client import Client

class Bank:

    def __init__(
            self
    ) -> None:
        self.clients = []

    def get_client(
            self,
            client_id: int
    ) -> Client | None:
        for client in self.clients:
            if client.client_id == client_id:
                return client
        raise ValueError(f"No client found with id {client_id}.")

    def add_client(
            self,
            client: Client
    ) -> None:
        if not isinstance(client, Client):
            raise TypeError("Only Client objects can be added.")
        self.clients.append(client)

    def remove_client(
            self,
            client_id: int
    ) -> None:
        client = self.get_client(client_id)
        if client:
            self.clients.remove(client)

    def print_all_client_balances(self) -> None:
        for client in self.clients:
            print(client.balance)
