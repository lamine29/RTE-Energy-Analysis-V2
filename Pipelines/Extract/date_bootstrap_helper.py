from datetime import datetime, timedelta
import pandas as pd

def generate_trimester_table(start_date_str):
    """
    Given a start date string in 'YYYY-MM-DD' format, return a pandas DataFrame with columns ['trimester', 'start_date', 'end_date'].
    Each trimester's end date is either the calculated trimester end or the current date, whichever is earlier.
    Dates are in 'YYYY-MM-DDT00:00:00+01:00' format.
    """
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


