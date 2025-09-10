import os    
from Pipelines.Extract.exctract_actual_generation import fetch_actual_generations_per_production_type, get_token
from Pipelines.Load.load_data import save_api_response_to_bronze
from Pipelines.Extract.api_connector import APIConnector    
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table

if __name__ == "__main__":
    # Initialize API connector
    api_connector = APIConnector()
    # Get token
    token = get_token(api_connector)
    start_date = "2024-01-01"

    # Generate trimester table from start_date to today
    trimester_table = generate_trimester_table(start_date)

    for _, row in trimester_table.iterrows():
        t_start = row['start_date']
        t_end = row['end_date']
        print(f"Fetching data for trimester: {t_start} to {t_end}")
        response = fetch_actual_generations_per_production_type(token, t_start, t_end, api_connector)
        save_api_response_to_bronze(response, f"actual_generations_per_production_type_{t_start}_to_{t_end}")