# pipelines/load.py
# Functions to load RTE API data into SQLite tables

# Load actual generation per production type
# Each entry contains start/end date, production type, and a list of values (with timestamps and value)
def load_actual_generations_per_production_type(data, db_path, table_name="actual_generations_per_production_type"):
    import sqlite3
    from datetime import datetime
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            end_date TEXT,
            production_type TEXT,
            value_start_date TEXT,
            value_end_date TEXT,
            value INTEGER,
            updated_date TEXT
        );
    """)
    for entry in data.get("actual_generations_per_production_type", []):
        start_date = entry.get("start_date")
        end_date = entry.get("end_date")
        production_type = entry.get("production_type")
        for v in entry.get("values", []):
            cur.execute(f"""
                INSERT INTO {table_name} (start_date, end_date, production_type, value_start_date, value_end_date, value, updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                start_date,
                end_date,
                production_type,
                v.get("start_date"),
                v.get("end_date"),
                v.get("value"),
                v.get("updated_date")
            ))
    conn.commit()
    print(f"Data loaded into {table_name} successfully.")
    cur.close()
    conn.close()

# Load actual generation per unit
# Each entry contains start/end date, unit info (EIC code, name), and a list of values (with timestamps and value)
def load_actual_generations_per_unit(data, db_path, table_name="actual_generations_per_unit"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            end_date TEXT,
            eic_code TEXT,
            unit_name TEXT,
            value_start_date TEXT,
            value_end_date TEXT,
            value INTEGER,
            updated_date TEXT
        );
    """)
    for entry in data.get("actual_generations_per_unit", []):
        start_date = entry.get("start_date")
        end_date = entry.get("end_date")
        unit = entry.get("unit", {})
        eic_code = unit.get("eic_code")
        unit_name = unit.get("name")
        for v in entry.get("values", []):
            cur.execute(f"""
                INSERT INTO {table_name} (start_date, end_date, eic_code, unit_name, value_start_date, value_end_date, value, updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                start_date,
                end_date,
                eic_code,
                unit_name,
                v.get("start_date"),
                v.get("end_date"),
                v.get("value"),
                v.get("updated_date")
            ))
    conn.commit()
    print(f"Data loaded into {table_name} successfully.")
    cur.close()
    conn.close()

# Load water reserves data
# Each entry contains start/end date and a list of values (with timestamps and value)
def load_water_reserves(data, db_path, table_name="water_reserves"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            end_date TEXT,
            value_start_date TEXT,
            value_end_date TEXT,
            value INTEGER,
            updated_date TEXT
        );
    """)
    for entry in data.get("water_reserves", []):
        start_date = entry.get("start_date")
        end_date = entry.get("end_date")
        for v in entry.get("values", []):
            cur.execute(f"""
                INSERT INTO {table_name} (start_date, end_date, value_start_date, value_end_date, value, updated_date)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                start_date,
                end_date,
                v.get("start_date"),
                v.get("end_date"),
                v.get("value"),
                v.get("updated_date")
            ))
    conn.commit()
    print(f"Data loaded into {table_name} successfully.")
    cur.close()
    conn.close()

# Load generation mix 15min time scale data
# Each entry contains start/end date, production type/subtype, and a list of values (with timestamps and value)
def load_generation_mix_15min_time_scale(data, db_path, table_name="generation_mix_15min_time_scale"):
    import sqlite3
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            start_date TEXT,
            end_date TEXT,
            production_type TEXT,
            production_subtype TEXT,
            value_start_date TEXT,
            value_end_date TEXT,
            value INTEGER,
            updated_date TEXT
        );
    """)
    for entry in data.get("generation_mix_15min_time_scale", []):
        start_date = entry.get("start_date")
        end_date = entry.get("end_date")
        production_type = entry.get("production_type")
        production_subtype = entry.get("production_subtype")
        for v in entry.get("values", []):
            cur.execute(f"""
                INSERT INTO {table_name} (start_date, end_date, production_type, production_subtype, value_start_date, value_end_date, value, updated_date)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                start_date,
                end_date,
                production_type,
                production_subtype,
                v.get("start_date"),
                v.get("end_date"),
                v.get("value"),
                v.get("updated_date")
            ))
    conn.commit()
    print(f"Data loaded into {table_name} successfully.")
    cur.close()
    conn.close()