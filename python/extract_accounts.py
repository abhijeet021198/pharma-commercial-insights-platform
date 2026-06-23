import pandas as pd

# Simulated API Response
accounts_data = [
    {
        "account_id": "ACC001",
        "account_name": "Apollo Hospital",
        "account_type": "Hospital",
        "city": "Mumbai",
        "state": "Maharashtra",
        "region": "West"
    },
    {
        "account_id": "ACC002",
        "account_name": "Fortis Hospital",
        "account_type": "Hospital",
        "city": "Pune",
        "state": "Maharashtra",
        "region": "West"
    }
]

# Convert API response to DataFrame
df = pd.DataFrame(accounts_data)

# Save as CSV
df.to_csv("data/accounts.csv", index=False)

print("Accounts data extracted successfully")
