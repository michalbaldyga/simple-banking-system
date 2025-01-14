from src.client import Client


class Bank:
    """
    A class used to represent a Bank.

    Methods
    -------
    get_client(client_id: int) -> Client
        - Retrieves a client with the specified client ID.
    add_client(client: Client) -> None
        - Adds a new client to the src.
    remove_client(client_id: int) -> None
        - Removes a client with the specified client ID from the src.
    print_all_client_balances() -> None
        - Prints the balance of all src clients.
    """

    def __init__(
            self
    ) -> None:
        """Initializes src."""
        self.clients = []

    def __repr__(self):
        return f"Bank(clients={self.clients})"

    def get_client(
            self,
            client_id: int
    ) -> Client:
        """Retrieves a client with the specified client ID.

        Parameters
        ----------
        client_id : int
            The unique id for the client.

        Returns
        -------
        Client
            Client object with specified client ID.

        Raises
        ------
        ValueError
            If there is no client with specified ID.
        """
        for client in self.clients:
            if client.client_id == client_id:
                return client
        raise ValueError(f"No client found with id {client_id}.")

    def add_client(
            self,
            client: Client
    ) -> None:
        """Adds a new client to the src.

        Parameters
        ----------
        client : Client
            Client object to be added to the src.

        Raises
        ------
        TypeError
            If the provided object is not an instance of the Client class.
        """
        if not isinstance(client, Client):
            raise TypeError("Only Client objects can be added.")
        self.clients.append(client)

    def remove_client(
            self,
            client_id: int
    ) -> None:
        """Removes a client with the specified client ID from the src.

        Parameters
        ----------
        client_id : int
            The unique ID for the client to be removed.
        """
        client = self.get_client(client_id)
        if client:
            self.clients.remove(client)

    def print_all_client_balances(
            self
    ) -> None:
        """Prints the balance of all src clients."""
        if not self.clients:
            print("There are no src clients.")
        else:
            print("The balance of all src clients:")
            for client in self.clients:
                print(client)
