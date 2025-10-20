import os
import json
import shutil
from datetime import datetime
import pandas as pd
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def save_api_response_as_raw_data(api_response, api_name, raw_data_dir):
    """
    Transform the API response directly to CSV and save it in the raw folder.
    Handles nested JSON structures and provides detailed logging.
    """
    try:
        logging.info(f"Processing API response for {api_name}")
        os.makedirs(raw_data_dir, exist_ok=True)
        
        if api_response is None:
            logging.error(f"Received None response for {api_name}")
            return None
            
        # Extract the values list from the API response
        if isinstance(api_response, dict):
            # Handle nested structure where data is in a list under a key
            # First, try to get the data directly if it's already flat
            if all(not isinstance(v, (dict, list)) for v in api_response.values()):
                data = [api_response]
            else:
                # Look for the first list in the response
                for key, value in api_response.items():
                    if isinstance(value, list):
                        data = value
                        break
                else:
                    # If no list found, use the dict as is
                    data = [api_response]
        elif isinstance(api_response, list):
            data = api_response
        else:
            data = [api_response]
        
        # Convert to DataFrame and handle nested dictionaries
        df = pd.json_normalize(data)
        
        # Log the DataFrame shape and columns
        logging.info(f"Created DataFrame with shape {df.shape} and columns: {df.columns.tolist()}")
        
        # Save as CSV
        filename = f"{api_name}.csv"
        file_path = os.path.join(raw_data_dir, filename)
        df.to_csv(file_path, index=False)
        
        logging.info(f"Successfully saved data to {file_path}")
        return file_path
        
    except Exception as e:
        logging.error(f"Error processing {api_name}: {str(e)}")
        raise








