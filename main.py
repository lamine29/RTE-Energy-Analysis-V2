import os    
from Pipelines.Extract.exctract_actual_generation import fetch_actual_generations_per_production_type, get_token
from Pipelines.Load.load_data_helper import save_api_response_to_bronze
from Pipelines.Extract.api_connector import APIConnector    
from Pipelines.Extract.date_bootstrap_helper import generate_trimester_table
from Pipelines.Load.load_actual_generation import load_actual_generations_per_production_type
from Pipelines.Load.load_generation_forecast import load_generation_forecast

if __name__ == "__main__":
    # Initialize API connector
    api_connector = APIConnector()
    # Get token
    token = get_token(api_connector)
    start_date = "2025-06-01"

    # Load actual generations per production type
    load_actual_generations_per_production_type(token,api_connector,start_date)
    load_generation_forecast(token, api_connector, start_date)
