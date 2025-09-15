from Pipelines.Load.load_data_helper import save_api_response_to_bronze
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table, generate_week_table, generate_year_table, generate_biweekly_table
import os
from Pipelines.Extract.extract_unavailabity import fetch_network_unavailability , fetch_generation_unavailability,fetch_other_market_information

# Load unavailability due to network unavailability for each year and save as JSON in bronze folder
def load_network_unavailability(token, api_connector, start_date): 
    # Always use this folder structure
    abs_dir = os.path.abspath("data/bronze_data/unavailabity/network_transmission_unavailability")
    # Use yearly table to fetch data
    year_table = generate_year_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for: {t_start} to {t_end}")
        response = fetch_network_unavailability(token, t_start[:10], t_end[:10], api_connector)
        filename = f"network_transmission_unavailability{t_start}_to_{t_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load unavailability due to generation unavailability for each year and save as JSON in bronze folder
def load_generation_unavailability(token, api_connector, start_date): 
    # Always use this folder structure
    abs_dir = os.path.abspath("data/bronze_data/unavailabity/generation_unavailability")
    # Use yearly table to fetch data
    year_table = generate_year_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for: {t_start} to {t_end}")
        response = fetch_generation_unavailability(token, t_start[:10], t_end[:10], api_connector)
        filename = f"generation_unavailabilty{t_start}_to_{t_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load unavailability due to generation unavailability for each year and save as JSON in bronze folder
def load_other_market_information(token, api_connector, start_date): 
    # Always use this folder structure
    abs_dir = os.path.abspath("data/bronze_data/unavailabity/other_market_information")
    # Use yearly table to fetch data
    year_table = generate_year_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for : {t_start} to {t_end}")
        response = fetch_other_market_information(token, t_start[:10], t_end[:10], api_connector)
        filename = f"other_market_information{t_start}_to_{t_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")