from Pipelines.Extract.api_connector import APIConnector    
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv()

def get_token(api_connector):
    return api_connector.get_access_token()

# Function to fetch actual generations per production type

def fetch_generation_forecast(token, start_date, end_date, api_connector):
    # Concatenate the required time and offset to the date strings
    start_date_fmt = start_date + "T00:00:00+01:00"
    end_date_fmt = end_date + "T00:00:00+01:00"
    url = f"https://digital.iservices.rte-france.com/open_api/generation_forecast/v3/forecasts?type=D-1&start_date={start_date_fmt}&end_date={end_date_fmt}"
    print("Request URL:", url)
    try:
        # Only for interval check, not for API call
        start_dt = datetime.strptime(start_date[:10], "%Y-%m-%d")
        end_dt = datetime.strptime(end_date[:10], "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval >= 15:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be < 155 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    response = api_connector.get_api_response(url, token)
    return response

