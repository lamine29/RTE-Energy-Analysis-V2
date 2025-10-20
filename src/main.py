import os    
from pipelines.Extract.exctract_actual_generation import fetch_actual_generations_per_production_type, get_token
from pipelines.Load.load_data_helper import save_api_response_to_bronze
from pipelines.Extract.api_connector import APIConnector    
from pipelines.Extract.date_bootstrap_helper import generate_trimester_table
from pipelines.Load.load_actual_generation import load_actual_generations_per_production_type, load_actual_generations_per_unit,load_actual_water_reserves,load_actual_generation_mix_15min_time_scale
from pipelines.Load.load_generation_forecast import load_generation_forecast
from pipelines.Load.load_generation_capacities import load_generation_capacities_per_production_type, load_generation_capacities_per_production_unit, load_generation_capacities_cpc


if __name__ == "__main__":
    # Initialize API connector
    api_connector = APIConnector()
    # Get token
    token = get_token(api_connector)
    start_date = "2020-01-01"

    # Load actual generations per production type
    load_actual_generations_per_production_type(token,api_connector,start_date)
    #load_generation_forecast(token, api_connector, start_date)
    #load_actual_generations_per_unit(token, api_connector, start_date)
    #load_actual_water_reserves(token, api_connector, start_date)
    #load_actual_generation_mix_15min_time_scale(token, api_connector, start_date)
    #load_generation_capacities_per_production_type(token, api_connector, start_date)
    #load_generation_capacities_per_production_unit(token, api_connector, start_date)
    #load_generation_capacities_cpc(token, api_connector, start_date)

    
    
