import requests
import pandas as pd

# OpenFDA API URL
url = "https://api.fda.gov/drug/drugsfda.json?limit=10"

print("Calling OpenFDA API...")

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    records = []

    for drug in data.get("results", []):
        records.append({
            "application_number": drug.get("application_number"),
            "sponsor_name": drug.get("sponsor_name")
        })

    df = pd.DataFrame(records)

    print("\nData Preview:")
    print(df.head())

    output_file = "data/openfda_drugs.csv"

    df.to_csv(output_file, index=False)

    print(f"\nCSV created successfully: {output_file}")

else:
    print(f"API call failed. Status Code: {response.status_code}")