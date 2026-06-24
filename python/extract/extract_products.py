import pandas as pd

# Simulated API Response
products_data = [
    {
        "product_id": "PROD001",
        "product_name": "Stelara",
        "brand": "Johnson & Johnson",
        "category": "Immunology"
    },
    {
        "product_id": "PROD002",
        "product_name": "Darzalex",
        "brand": "Johnson & Johnson",
        "category": "Oncology"
    }
]

# Convert API response to DataFrame
df = pd.DataFrame(products_data)

# Save as CSV
df.to_csv("data/products.csv", index=False)

print("Products data extracted successfully")
