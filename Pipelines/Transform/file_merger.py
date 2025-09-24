import os
import pandas as pd

def merge_csv_files_in_directory(directory_path, output_file_path=None):
    """
    Merges all CSV files in the given directory into a single CSV file.
    If output_file_path is not provided, saves as 'merged.csv' in the directory.
    """
    csv_files = [f for f in os.listdir(directory_path) if f.endswith('.csv')]
    if not csv_files:
        raise ValueError(f"No CSV files found in directory: {directory_path}")

    dataframes = []
    for csv_file in csv_files:
        file_path = os.path.join(directory_path, csv_file)
        df = pd.read_csv(file_path)
        dataframes.append(df)

    merged_df = pd.concat(dataframes, ignore_index=True)

    if output_file_path is None:
        output_file_path = os.path.join(directory_path, 'merged.csv')

    merged_df.to_csv(output_file_path, index=False)
    return output_file_path
