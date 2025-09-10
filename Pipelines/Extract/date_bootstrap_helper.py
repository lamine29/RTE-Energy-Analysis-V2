from datetime import datetime, timedelta
import pandas as pd

def generate_trimester_table(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.now()
    rows = []
    i = 0
    while True:
        t_start = start_date + timedelta(days=92 * i)
        t_end = t_start + timedelta(days=91)
        if t_start > today:
            break
        # Clamp t_end to today if it exceeds today
        t_end = min(t_end, today)
        t_start_fmt = t_start.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        t_end_fmt = t_end.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        rows.append({
            'trimester': i + 1,
            'start_date': t_start_fmt,
            'end_date': t_end_fmt
        })
        if t_end >= today:
            break
        i += 1
    return pd.DataFrame(rows)

def generate_week_table(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.now()
    rows = []
    i = 0
    while True:
        w_start = start_date + timedelta(days=7 * i)
        w_end = w_start + timedelta(days=6)
        if w_start > today:
            break
        # Clamp w_end to today if it exceeds today
        w_end = min(w_end, today)
        w_start_fmt = w_start.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        w_end_fmt = w_end.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        rows.append({
            'week': i + 1,
            'start_date': w_start_fmt,
            'end_date': w_end_fmt
        })
        if w_end >= today:
            break
        i += 1
    return pd.DataFrame(rows)

def generate_year_table(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.now()
    rows = []
    i = 0
    while True:
        y_start = start_date + timedelta(days=365 * i)
        y_end = y_start + timedelta(days=364)
        if y_start > today:
            break
        # Clamp y_end to today if it exceeds today
        y_end = min(y_end, today)
        y_start_fmt = y_start.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        y_end_fmt = y_end.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        rows.append({
            'year': i + 1,
            'start_date': y_start_fmt,
            'end_date': y_end_fmt
        })
        if y_end >= today:
            break
        i += 1
    return pd.DataFrame(rows)

def generate_biweekly_table(start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
    today = datetime.now()
    rows = []
    i = 0
    while True:
        b_start = start_date + timedelta(days=14 * i)
        b_end = b_start + timedelta(days=13)
        if b_start > today:
            break
        # Clamp b_end to today if it exceeds today
        b_end = min(b_end, today)
        b_start_fmt = b_start.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        b_end_fmt = b_end.strftime("%Y-%m-%d") + "T00:00:00+01:00"
        rows.append({
            'biweek': i + 1,
            'start_date': b_start_fmt,
            'end_date': b_end_fmt
        })
        if b_end >= today:
            break
        i += 1
    return pd.DataFrame(rows)


