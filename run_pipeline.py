import os
import logging
import time
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

from Pipelines.Extract.api_connector import APIConnector
from Pipelines.Extract.exctract_actual_generation import get_token
from Pipelines.Load.load_actual_generation import (
    load_actual_generations_per_production_type,
    load_actual_generations_per_unit,
    load_actual_water_reserves,
    load_actual_generation_mix_15min_time_scale,
)
from Pipelines.Load.load_generation_forecast import load_generation_forecast
from Pipelines.Load.load_generation_capacities import (
    load_generation_capacities_per_production_type,
    load_generation_capacities_per_production_unit,
    load_generation_capacities_cpc,
)
from Pipelines.Load.load_unavailabilty import (
    load_generation_unavailability,
    load_network_unavailability,
    load_other_market_information,
)
from Pipelines.Load.load_data_to_silver import load_bronze_to_silver
from Pipelines.Load.load_data_to_gold import load_silver_to_gold

# Configure logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO'),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv('LOG_FILE', 'pipeline.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class Pipeline:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Initialize API connection
        self.api_connector = APIConnector()
        self.token = get_token(self.api_connector)
        
        # Get pipeline configuration from environment variables
        self.start_date = os.getenv('PIPELINE_START_DATE', '2020-01-01')
        self.bronze_path = os.getenv('BRONZE_PATH', '/data/bronze_data')
        self.silver_path = os.getenv('SILVER_PATH', '/data/silver_data')
        self.gold_path = os.getenv('GOLD_PATH', '/data/gold_data')
        
        # Number of retries for API calls
        self.max_retries = int(os.getenv('MAX_RETRIES', '3'))
        self.retry_delay = int(os.getenv('RETRY_DELAY', '5'))
        
        # Ensure data directories exist
        for path in [self.bronze_path, self.silver_path, self.gold_path]:
            Path(path).mkdir(parents=True, exist_ok=True)

    def run_with_retry(self, func, *args, **kwargs):
        """Run a function with retries"""
        for attempt in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise e
                logger.warning(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)

    def load_actual_generation_data(self):
        """Load actual generation data"""
        logger.info("Starting actual generation data load...")
        try:
            self.run_with_retry(load_actual_generations_per_production_type, 
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_actual_generations_per_unit,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_actual_water_reserves,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_actual_generation_mix_15min_time_scale,
                              self.token, self.api_connector, self.start_date)
            logger.info("Completed actual generation data load")
        except Exception as e:
            logger.error(f"Error in actual generation data load: {str(e)}")
            raise

    def load_generation_capacities(self):
        """Load generation capacities data"""
        logger.info("Starting generation capacities load...")
        try:
            self.run_with_retry(load_generation_capacities_per_production_type,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_generation_capacities_per_production_unit,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_generation_capacities_cpc,
                              self.token, self.api_connector, self.start_date)
            logger.info("Completed generation capacities load")
        except Exception as e:
            logger.error(f"Error in generation capacities load: {str(e)}")
            raise

    def load_unavailability_data(self):
        """Load unavailability data"""
        logger.info("Starting unavailability data load...")
        try:
            self.run_with_retry(load_network_unavailability,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_generation_unavailability,
                              self.token, self.api_connector, self.start_date)
            self.run_with_retry(load_other_market_information,
                              self.token, self.api_connector, self.start_date)
            logger.info("Completed unavailability data load")
        except Exception as e:
            logger.error(f"Error in unavailability data load: {str(e)}")
            raise

    def transform_data(self):
        """Transform data through bronze, silver, and gold layers"""
        logger.info("Starting data transformation...")
        try:
            self.run_with_retry(load_bronze_to_silver)
            self.run_with_retry(load_silver_to_gold)
            logger.info("Completed data transformation")
        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
            raise

    def run(self):
        """Run the complete pipeline"""
        start_time = datetime.now()
        logger.info(f"Starting pipeline run at {start_time}")
        
        try:
            # Execute pipeline steps sequentially
            self.load_actual_generation_data()
            self.load_generation_capacities()
            self.load_unavailability_data()
            self.transform_data()
            
            end_time = datetime.now()
            duration = end_time - start_time
            logger.info(f"Pipeline completed successfully at {end_time}. Duration: {duration}")
            return True
        except Exception as e:
            logger.error(f"Pipeline failed: {str(e)}")
            return False

if __name__ == "__main__":
    pipeline = Pipeline()
    success = pipeline.run()
    exit(0 if success else 1)
