from Pipelines.Extract.extract_generation_installed_cpc import fetch_generation_capacities_per_production_type, fetch_generation_capacities_per_production_unit, fetch_generation_capacities_cpc
from Pipelines.Load.load_data_helper import save_api_response_to_bronze
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table, generate_week_table, generate_year_table, generate_biweekly_table
import os

# Load generation capacities per production type for each year and save as JSON in bronze folder
def load_generation_capacities_per_production_type(token, api_connector, start_date):
    # Always use this folder structure
    abs_dir = os.path.abspath("data/bronze_data/generation_intalled_capacities/generation_capacities_per_production_type")
    # Use yearly table to fetch data
    year_table = generate_year_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for: {t_start} to {t_end}")
        response = fetch_generation_capacities_per_production_type(token, t_start[:10], t_end[:10], api_connector)
        filename = f"generation_capacities_per_production_type_{t_start}_to_{t_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load generation capacities per production unit for each week and save as JSON in bronze folder
def load_generation_capacities_per_production_unit(token, api_connector, start_date):
    abs_dir = os.path.abspath("data/bronze_data/generation_intalled_capacities/generation_capacities_per_production_unit")
    year_table = generate_week_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in week_table.iterrows():
        w_start = row['start_date']
        w_end = row['end_date']
        print(f"Fetching data for : {w_start} to {w_end}")
        response = fetch_generation_capacities_per_production_unit(token, w_start[:10], w_end[:10], api_connector)
        filename = f"generation_capacities_per_production_unit_{w_start}_to_{w_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

#load generation capacities cpc

def load_generation_capacities_cpc(token, api_connector, start_date):
    abs_dir = os.path.abspath("data/bronze_data/generation_intalled_capacities/generation_capacities_cpc")
    year_table = generate_week_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        w_start = row['start_date']
        w_end = row['end_date']
        print(f"Fetching data for : {w_start} to {w_end}")
        response = fetch_generation_capacities_cpc(token, w_start[:10], w_end[:10], api_connector)
        filename = f"generation_capacities_cpc_{w_start}_to_{w_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")