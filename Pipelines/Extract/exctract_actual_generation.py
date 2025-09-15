from Pipelines.Extract.api_connector import APIConnector    
from dotenv import load_dotenv
import os
from datetime import datetime
import json

load_dotenv()

# Function to get token

def get_token(api_connector):
    return api_connector.get_access_token()

# Function to fetch actual generations per production type

def fetch_actual_generations_per_production_type(token, start_date, end_date, api_connector):
    # Concatenate the required time and offset to the date strings
    start_date_fmt = start_date + "T00:00:00+01:00"
    end_date_fmt = end_date + "T00:00:00+01:00"
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type?start_date={start_date_fmt}&end_date={end_date_fmt}"
    print("Request URL:", url)
    try:
        # Only for interval check, not for API call
        start_dt = datetime.strptime(start_date[:10], "%Y-%m-%d")
        end_dt = datetime.strptime(end_date[:10], "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval >= 155:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be < 155 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    response = api_connector.get_api_response(url, token)
    return response

# Function to fetch actual generation per unit

def fetch_actual_generation_per_unit(token, start_date, end_date, api_connector):
    # Concatenate the required time and offset to the date strings
    start_date_fmt = start_date + "T00:00:00+01:00"
    end_date_fmt = end_date + "T00:00:00+01:00"
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_unit?start_date={start_date_fmt}&end_date={end_date_fmt}"
    print("Request URL:", url)
    try:
        # Only for interval check, not for API call
        start_dt = datetime.strptime(start_date[:10], "%Y-%m-%d")
        end_dt = datetime.strptime(end_date[:10], "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval > 7:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be <= 7 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    response = api_connector.get_api_response(url, token)
    return response

# Function to fetch actual water reserves

def fetch_actual_water_reserves(token, start_date, end_date, api_connector):
    # Concatenate the required time and offset to the date strings
    start_date_fmt = start_date + "T00:00:00+01:00"
    end_date_fmt = end_date + "T00:00:00+01:00"
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/water_reserves?start_date={start_date_fmt}&end_date={end_date_fmt}"
    print("Request URL:", url)
    try:
        # Only for interval check, not for API call
        start_dt = datetime.strptime(start_date[:10], "%Y-%m-%d")
        end_dt = datetime.strptime(end_date[:10], "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval > 365:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be <= 365 days)")
        now = datetime.now()
        if not (now.weekday() == 3 and now.hour == 13):
            print("fetch_actual_water_reserves can only be executed on Wednesday at 1pm.")
            return None
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    response = api_connector.get_api_response(url, token)
    return response

# Function to fetch actual generation mix 15 min time scale

def fetch_actual_generation_mix_15_min_time_scale(token, start_date, end_date, api_connector):
    # Concatenate the required time and offset to the date strings
    start_date_fmt = start_date + "T00:00:00+01:00"
    end_date_fmt = end_date + "T00:00:00+01:00"
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/eneration_mix_15min_time_scale?start_date={start_date_fmt}&end_date={end_date_fmt}"
    print("Request URL:", url)
    try:
        # Only for interval check, not for API call
        start_dt = datetime.strptime(start_date[:10], "%Y-%m-%d")
        end_dt = datetime.strptime(end_date[:10], "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval > 14:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be <= 14 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    response = api_connector.get_api_response(url, token)
    return response