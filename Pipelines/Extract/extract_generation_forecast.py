from pipelines.extraction.api_connector import APIConnector
import sqlite3
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

DB_PATH = os.getenv("DB_PATH", "data/energy_analysis.db")