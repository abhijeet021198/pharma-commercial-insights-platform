from pathlib import Path
import logging
import requests
import pandas as pd

# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_URL = "https://api.fda.gov/drug/drugsfda.json?limit=10"

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
LOG_DIR = PROJECT_ROOT / "logs"

OUTPUT_FILE = DATA_DIR / "openfda_drugs.csv"
LOG_FILE = LOG_DIR / "extract_openfda.log"

# --------------------------------------------------
# Logging Configuration
# --------------------------------------------------

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --------------------------------------------------
# Functions
# --------------------------------------------------

def extract_drug_data():
    logging.info("Starting OpenFDA extraction")

    response = requests.get(API_URL, timeout=30)

    response.raise_for_status()

    data = response.json()

    records = []

    for drug in data.get("results", []):
        records.append(
            {
                "application_number": drug.get("application_number"),
                "sponsor_name": drug.get("sponsor_name")
            }
        )

    df = pd.DataFrame(records)

    logging.info(f"Extracted {len(df)} records")

    return df


def save_to_csv(df):
    df.to_csv(OUTPUT_FILE, index=False)

    logging.info(f"CSV saved to {OUTPUT_FILE}")


# --------------------------------------------------
# Main
# --------------------------------------------------

def main():
    try:
        print("Extracting OpenFDA data...")

        df = extract_drug_data()

        print(df.head())

        save_to_csv(df)

        print(f"\nCSV created successfully: {OUTPUT_FILE}")

        logging.info("Pipeline completed successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {str(e)}")
        print(f"Error: {e}")


if __name__ == "__main__":
    main()