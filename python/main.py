import sys

from extract.extract_accounts import extract_accounts
from extract.extract_products import extract_products
from extract.extract_orders import extract_orders
from extract.extract_inventory import extract_inventory
from extract.extract_interactions import extract_interactions


COMMANDS = {
    "extract_accounts": extract_accounts,
    "extract_products": extract_products,
    "extract_orders": extract_orders,
    "extract_inventory": extract_inventory,
    "extract_interactions": extract_interactions,
}


def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        sys.exit(1)

    COMMANDS[command]()


if __name__ == "__main__":
    main()