from bank.bank import Bank
from bank.client import Client

def main():
    c1 = Client(1, 'Adam', 100)
    c2 = Client(2, 'Mada', 200)

    b = Bank()
    b.add_client(c1)
    b.add_client(c2)

    b.print_all_client_balances()

if __name__ == "__main__":
    main()
