import os
import json
import shutil
from datetime import datetime
import pandas as pd

def save_api_response_to_bronze(api_response, api_name, bronze_dir="data/bronze_data"):
    """
    Save the API response as a JSON file in the bronze folder inside the data directory.
    The filename includes only the API name for traceability.
    """
    os.makedirs(bronze_dir, exist_ok=True)
    filename = f"{api_name}.json"
    file_path = os.path.join(bronze_dir, filename)
    with open(file_path, "w") as f:
        json.dump(api_response, f, indent=2)
    return file_path

def move_csv_to_silver(data, filename, csv_dir="data/silver_data"):
    """
    Save the provided data as a CSV file in the silver folder.
    """
    os.makedirs(csv_dir, exist_ok=True)
    df = pd.DataFrame(data)
    csv_filename = filename.replace(".json", ".csv")
    csv_path = os.path.join(csv_dir, csv_filename)
    df.to_csv(csv_path, index=False)
    print(f"Transformed {filename} to {csv_filename}")



