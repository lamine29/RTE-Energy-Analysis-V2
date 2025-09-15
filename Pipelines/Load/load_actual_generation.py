from Pipelines.Extract.exctract_actual_generation import fetch_actual_generations_per_production_type, get_token, fetch_actual_generation_per_unit, fetch_actual_water_reserves, fetch_actual_generation_mix_15_min_time_scale
from Pipelines.Extract.api_connector import APIConnector
from Pipelines.Load.load_data_helper import save_api_response_to_bronze
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table, generate_week_table, generate_year_table, generate_biweekly_table
import os

# Load actual generation per production type for each trimester and save as JSON in bronze folder
def load_actual_generations_per_production_type(token, api_connector, start_date):
    # Always use this folder structure
    abs_dir = os.path.abspath("data/bronze_data/actual_generation/actual_generations_per_production_type")
    trimester_table = generate_trimester_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in trimester_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for : {t_start} to {t_end}")
        response = fetch_actual_generations_per_production_type(token, t_start[:10], t_end[:10], api_connector)
        filename = f"actual_generations_per_production_type_{t_start}_to_{t_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load actual generation per unit for each week and save as JSON in bronze folder
def load_actual_generations_per_unit(token, api_connector, start_date):
    abs_dir = os.path.abspath("data/bronze_data/actual_generation/actual_generations_per_unit")
    week_table = generate_week_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in week_table.iterrows():
        w_start = row['start_date']
        w_end = row['end_date']
        print(f"Fetching data for : {w_start} to {w_end}")
        response = fetch_actual_generation_per_unit(token, w_start[:10], w_end[:10], api_connector)
        filename = f"actual_generations_per_unit_{w_start}_to_{w_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load actual water reserves for each year and save as JSON in bronze folder
def load_actual_water_reserves(token, api_connector, start_date):
    abs_dir = os.path.abspath("data/bronze_data/actual_generation/actual_water_reserves")
    year_table = generate_year_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in year_table.iterrows():
        y_start = row['start_date']
        y_end = row['end_date']
        print(f"Fetching data for : {y_start} to {y_end}")
        response = fetch_actual_water_reserves(token, y_start[:10], y_end[:10], api_connector)
        filename = f"actual_water_reserves_{y_start}_to_{y_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")

# Load actual generation mix 15min for each bi-week and save as JSON in bronze folder
def load_actual_generation_mix_15min_time_scale(token, api_connector, start_date):
    abs_dir = os.path.abspath("data/bronze_data/actual_generation/actual_generation_mix_15min_time_scale")
    biweekly_table = generate_biweekly_table(start_date)
    os.makedirs(abs_dir, exist_ok=True)
    for _, row in biweekly_table.iterrows():
        b_start = row['start_date']
        b_end = row['end_date']
        print(f"Fetching data for : {b_start} to {b_end}")
        response = fetch_actual_generation_mix_15_min_time_scale(token, b_start[:10], b_end[:10], api_connector)
        filename = f"actual_generation_mix_15min_time_scale_{b_start}_to_{b_end}"
        save_api_response_to_bronze(response, filename, bronze_dir=abs_dir)
        print(f"Saved: {filename}.json in {abs_dir}")
