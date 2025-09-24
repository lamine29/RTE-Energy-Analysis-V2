import os
import json
import pandas as pd

def json_to_csv(json_file_path, csv_file_path=None):
    """
    Transforms a JSON file (array of records or dict) to a CSV file.
    If csv_file_path is not provided, saves with the same name as the JSON file but with .csv extension.
    """
    if not os.path.exists(json_file_path):
        raise FileNotFoundError(f"JSON file not found: {json_file_path}")

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # If the data is a dict with a single key containing the records, extract it
    if isinstance(data, dict) and len(data) == 1:
        data = list(data.values())[0]

    df = pd.DataFrame(data)

    if csv_file_path is None:
        csv_file_path = os.path.splitext(json_file_path)[0] + '.csv'

    df.to_csv(csv_file_path, index=False)
    return csv_file_path

def csv_to_json(csv_file_path, json_file_path=None):
    """
    Transforms a CSV file to a JSON file (array of records).
    If json_file_path is not provided, saves with the same name as the CSV file but with .json extension.
    """
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"CSV file not found: {csv_file_path}")

    df = pd.read_csv(csv_file_path)

    if json_file_path is None:
        json_file_path = os.path.splitext(csv_file_path)[0] + '.json'

    df.to_json(json_file_path, orient='records', force_ascii=False, indent=2)
    return json_file_path
