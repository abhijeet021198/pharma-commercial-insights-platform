import pandas as pd

# Simulated API Response
inventory_data = [
    {
        "product_id": "PROD001",
        "inventory_date": "2026-01-05",
        "stock_quantity": 5000
    },
    {
        "product_id": "PROD002",
        "inventory_date": "2026-01-05",
        "stock_quantity": 3500
    }
]

# Convert API response to DataFrame
df = pd.DataFrame(inventory_data)

# Data Validation
df = df[df["stock_quantity"] >= 0]

# Save as CSV
df.to_csv("data/inventory.csv", index=False)

print("Inventory data extracted successfully")
