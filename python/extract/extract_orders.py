import pandas as pd

def extract_orders():
    # Simulated API Response
    orders_data = [
        {
            "order_id": "ORD001",
            "account_id": "ACC001",
            "product_id": "PROD001",
            "rep_id": "REP001",
            "order_date": "2026-01-05",
            "quantity": 50,
            "revenue": 250000
        },
        {
            "order_id": "ORD002",
            "account_id": "ACC002",
            "product_id": "PROD002",
            "rep_id": "REP001",
            "order_date": "2026-01-06",
            "quantity": 25,
            "revenue": 180000
        }
    ]

    # Convert API response to DataFrame
    df = pd.DataFrame(orders_data)

    # Basic Data Validation
    df = df[df["quantity"] > 0]
    df = df[df["revenue"] > 0]

    # Save as CSV
    df.to_csv("data/orders.csv", index=False)

    print("Orders data extracted successfully")

if __name__ == "__main__":
    extract_orders()