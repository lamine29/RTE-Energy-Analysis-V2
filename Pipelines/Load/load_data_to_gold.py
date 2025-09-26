import os
from Pipelines.Transform.file_merger import merge_csv_files_in_directory

def load_silver_to_gold(silver_root='data/silver_data', gold_root='data/gold_data'):
    """
    For each directory in silver_root, merge all CSV files inside it into a single CSV file in the corresponding
    gold_data directory using merge_csv_files_in_directory.
    """
    for dirpath, dirnames, filenames in os.walk(silver_root):
        csv_files = [f for f in filenames if f.endswith('.csv')]
        if not csv_files:
            continue
        rel_path = os.path.relpath(dirpath, silver_root)
        gold_dir = os.path.join(gold_root, rel_path)
        os.makedirs(gold_dir, exist_ok=True)
        output_file_path = os.path.join(gold_dir, 'merged.csv')
        try:
            merge_csv_files_in_directory(dirpath, output_file_path)
        except Exception as e:
            print(f"Failed to merge CSVs in {dirpath}: {e}")
    print(f"All merged CSV files are now in {gold_root}.")
