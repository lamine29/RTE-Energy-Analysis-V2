import os    
from pipelines.Extract.api_connector import APIConnector    
from pipelines.Load.load_actual_generation import load_actual_generations_per_production_type, load_actual_generations_per_unit,load_actual_water_reserves,load_actual_generation_mix_15min_time_scale
from pipelines.Load.load_generation_forecast import load_generation_forecast
from pipelines.Load.load_generation_capacities import load_generation_capacities_per_production_type, load_generation_capacities_per_production_unit, load_generation_capacities_cpc
from pipelines.Load.load_unavailabilty import load_generation_unavailability, load_network_unavailability, load_other_market_information
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def run_data_ingestion():
    # Initialize API connector
    logging.info("Initializing API connector...")
    api_connector = APIConnector()
    
    # Get token
    logging.info("Getting authentication token...")
    token = APIConnector.get_access_token(api_connector)
    start_date = "2020-01-01"

    # Define pipeline steps with descriptive names
    pipeline_steps = [
       # ("Actual generations per production type", lambda: load_actual_generations_per_production_type(token, api_connector, start_date)),
        #("Generation forecast", lambda: load_generation_forecast(token, api_connector, start_date)),
        #("Actual generations per unit", lambda: load_actual_generations_per_unit(token, api_connector, start_date)),
        #("Actual water reserves", lambda: load_actual_water_reserves(token, api_connector, start_date)),
        #("Actual generation mix 15min", lambda: load_actual_generation_mix_15min_time_scale(token, api_connector, start_date)),
        ("Generation capacities per production type", lambda: load_generation_capacities_per_production_type(token, api_connector, start_date)),
        #("Generation capacities per production unit", lambda: load_generation_capacities_per_production_unit(token, api_connector, start_date)),
        #("Generation capacities CPC", lambda: load_generation_capacities_cpc(token, api_connector, start_date)),
        #("Network unavailability", lambda: load_network_unavailability(token, api_connector, start_date)),
        #("Generation unavailability", lambda: load_generation_unavailability(token, api_connector, start_date)),
        #("Other market information", lambda: load_other_market_information(token, api_connector, start_date))
    ]

    # Execute pipeline steps sequentially with failure handling
    total_steps = len(pipeline_steps)
    last_completed_step = -1  # Start from beginning by default
    
    # Try to read last completed step from file
    status_file = "pipeline_status.txt"
    if os.path.exists(status_file):
        try:
            with open(status_file, 'r') as f:
                last_completed_step = int(f.read().strip())
            logging.info(f"Resuming from step {last_completed_step + 2}")
        except:
            logging.warning("Could not read status file, starting from beginning")
    
    for index, (step_name, step_function) in enumerate(pipeline_steps, 1):
        # Skip already completed steps
        if index <= last_completed_step + 1:
            logging.info(f"Skipping completed step {index}/{total_steps}: {step_name}")
            continue
            
        try:
            logging.info(f"[{index}/{total_steps}] Starting: {step_name}")
            start_time = datetime.now()
            
            step_function()
            
            duration = datetime.now() - start_time
            logging.info(f"[{index}/{total_steps}] Completed: {step_name} (Duration: {duration})")
            
            # Save progress
            with open(status_file, 'w') as f:
                f.write(str(index - 1))
                
        except Exception as e:
            logging.error(f"Error in step {step_name}: {str(e)}")
            logging.error("Pipeline stopped. Run again to resume from this point.")
            raise

    logging.info("Data ingestion pipeline completed successfully!")


 