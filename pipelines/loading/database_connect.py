import sqlite3
import os


def get_db_connection_and_cursor(db_path=None):
    """
    Establishes and returns a connection and cursor to the SQLite database.
    If db_path is not provided, uses the default path from environment or 'data/energy_analysis.db'.
    """
    if db_path is None:
        db_path = os.getenv("DB_PATH", "data/energy_analysis.db")
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return conn, cur


def close_db_connection(conn, cur):
    """
    Closes the cursor and connection to the SQLite database.
    """
    if cur:
        cur.close()
    if conn:
        conn.close()