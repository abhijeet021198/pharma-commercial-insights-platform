import pandas as pd

# Simulated API Response
interactions_data = [
    {
        "interaction_id": "INT001",
        "account_id": "ACC001",
        "rep_id": "REP001",
        "interaction_date": "2026-01-03",
        "interaction_type": "Visit"
    },
    {
        "interaction_id": "INT002",
        "account_id": "ACC002",
        "rep_id": "REP001",
        "interaction_date": "2026-01-04",
        "interaction_type": "Call"
    }
]

# Convert API response to DataFrame
df = pd.DataFrame(interactions_data)

# Valid interaction types
valid_interaction_types = ["Visit", "Call", "Email"]

# Data Validation
df = df[df["interaction_type"].isin(valid_interaction_types)]

# Save as CSV
df.to_csv("data/interactions.csv", index=False)

print("Interactions data extracted successfully")
