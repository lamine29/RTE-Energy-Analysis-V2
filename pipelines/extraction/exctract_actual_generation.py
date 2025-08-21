from pipelines.extraction.api_connector import APIConnector
import sqlite3
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/energy_analysis.db")

# Function to get token

def get_token(api_connector):
    return api_connector.get_access_token()

# Function to fetch actual generations per production type

def fetch_actual_generations_per_production_type(token, start_date, end_date, api_connector):
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_production_type?start_date={start_date}&end_date={end_date}"
    print("Request URL:", url)
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval >= 155:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be < 155 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    return api_connector.get_api_response(url, token)

# Function to fetch actual generation per unit

def fetch_actual_generation_per_unit(token, start_date, end_date, api_connector):
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/actual_generations_per_unit?start_date={start_date}&end_date={end_date}"
    print("Request URL:", url)
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval > 7:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be <= 7 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    return api_connector.get_api_response(url, token)

# Function to fetch actual water reserves

def fetch_actual_water_reserves(token, start_date, end_date, api_connector):
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/water_reserves?start_date={start_date}&end_date={end_date}"
    print("Request URL:", url)
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
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
    return api_connector.get_api_response(url, token)

# Function to fetch actual generation mix 15 min time scale

def fetch_actual_generation_mix_15_min_time_scale(token, start_date, end_date, api_connector):
    url = f"https://digital.iservices.rte-france.com/open_api/actual_generation/v1/eneration_mix_15min_time_scale?start_date={start_date}&end_date={end_date}"
    print("Request URL:", url)
    try:
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        interval = (end_dt - start_dt).days
        if interval > 14:
            raise ValueError(f"Interval between start_date and end_date is {interval} days, which is not allowed (must be <= 14 days)")
    except Exception as e:
        print(f"Date parsing error: {e}")
        raise
    return api_connector.get_api_response(url, token)