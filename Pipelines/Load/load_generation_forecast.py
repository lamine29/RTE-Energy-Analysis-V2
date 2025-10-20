from pipelines.Extract.extract_generation_forecast import fetch_generation_forecast
from pipelines.Load.load_data_helper import save_api_response_as_raw_data
from pipelines.Extract.date_bootstrap_helper import generate_trimester_table, generate_week_table, generate_year_table, generate_biweekly_table
import os

# Load actual generation per production type for each trimester and save as JSON in bronze folder
def load_generation_forecast(token, api_connector, start_date):
    # Always use this folder structure
    abs_dir = os.path.abspath("data/raw/generation_forecast")
    biweekly_table = generate_biweekly_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in biweekly_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for : {t_start} to {t_end}")
        response = fetch_generation_forecast(token, t_start[:10], t_end[:10], api_connector)
        filename = f"partition_generation_forecast_{t_start}_to_{t_end}"
        save_api_response_as_raw_data(response, filename, raw_data_dir=abs_dir)
        print(f"Saved: {filename}.csv in {abs_dir}")