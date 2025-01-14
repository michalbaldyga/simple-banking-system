from client import Client

class Bank:
    """
    A class used to represent a Bank.

    Methods
    -------
    get_client(client_id: int) -> Client
        - Retrieves a client with the specified client ID.
    add_client(client: Client) -> None
        - Adds a new client to the bank.
    remove_client(client_id: int) -> None
        - Removes a client with the specified client ID from the bank.
    print_all_client_balances() -> None
        - Prints the balance of all bank clients.
    """

    def __init__(
            self
    ) -> None:
        """Initializes bank."""
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
        """Adds a new client to the bank.

        Parameters
        ----------
        client : Client
            Client object to be added to the bank.

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
        """Removes a client with the specified client ID from the bank.

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
        """Prints the balance of all bank clients."""
        if not self.clients:
            print("There are no bank clients.")
        else:
            print("The balance of all bank clients:")
            for client in self.clients:
                print(client)
