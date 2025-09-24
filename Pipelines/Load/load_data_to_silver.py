import os
from Pipelines.Transform.file_transform_helper import json_to_csv

def bronze_to_silver(bronze_root='data/bronze_data', silver_root='data/silver_data'):
    """
    For each directory in bronze_root, recreate the directory structure in silver_root and
    transform all JSON files to CSV using json_to_csv.
    """
    for dirpath, dirnames, filenames in os.walk(bronze_root):
        # Compute the corresponding path in silver_root
        rel_path = os.path.relpath(dirpath, bronze_root)
        silver_dir = os.path.join(silver_root, rel_path)
        os.makedirs(silver_dir, exist_ok=True)
        for filename in filenames:
            if filename.endswith('.json'):
                bronze_file = os.path.join(dirpath, filename)
                csv_filename = os.path.splitext(filename)[0] + '.csv'
                silver_file = os.path.join(silver_dir, csv_filename)
                try:
                    json_to_csv(bronze_file, silver_file)
                except Exception as e:
                    print(f"Failed to convert {bronze_file} to CSV: {e}")
