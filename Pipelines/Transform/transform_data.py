import os
import json
import pandas as pd
from Pipelines.Load.load_data_helper import move_csv_to_silver

def transform_bronze_json_to_csv(bronze_dir="data/bronze_data", csv_dir="data/silver_data"):
    """
    Transforms all JSON files in the bronze folder into CSV files in the silver_data folder.
    Each JSON file is expected to be a list of records or a dict with a top-level list.
    """
    os.makedirs(csv_dir, exist_ok=True)
    for filename in os.listdir(bronze_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(bronze_dir, filename)
            with open(json_path, "r") as f:
                data = json.load(f)
            # Try to find the main data list
            if isinstance(data, dict):
                for v in data.values():
                    if isinstance(v, list):
                        data = v
                        break
            if not isinstance(data, list):
                print(f"Skipping {filename}: not a list of records.")
                continue
            # move_csv_to_silver(data, filename, csv_dir)  # No longer called here
    print("All CSV files are now ready to be moved in the silver_data folder.")
