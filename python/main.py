import sys


def extract_accounts():
    print("Running Accounts Extraction...")


def extract_products():
    print("Running Products Extraction...")


def extract_orders():
    print("Running Orders Extraction...")


def extract_inventory():
    print("Running Inventory Extraction...")


def extract_interactions():
    print("Running Interactions Extraction...")


def load_bronze():
    print("Loading Bronze Tables...")


COMMANDS = {
    "extract_accounts": extract_accounts,
    "extract_products": extract_products,
    "extract_orders": extract_orders,
    "extract_inventory": extract_inventory,
    "extract_interactions": extract_interactions,
    "load_bronze": load_bronze,
}


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <command>")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    command = sys.argv[1]

    if command not in COMMANDS:
        print(f"Unknown command: {command}")
        sys.exit(1)

    COMMANDS[command]()


if __name__ == "__main__":
    main()