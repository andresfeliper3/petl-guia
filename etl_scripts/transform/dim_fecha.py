import petl as etl
from datetime import datetime, timedelta


def generate_dates(start_date, num_rows):
    return (start_date + timedelta(days=x) for x in range(num_rows))

def get_day_name(date):
    day_names = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    return day_names[date.weekday()]

def crear_dim_fecha():
    # Start date
    start_date = datetime(2000, 1, 1)

    # Number of rows
    num_rows = 10000

    # Generate a sequence of dates and create a table
    table = etl.fromdicts([{'date': date} for date in generate_dates(start_date, num_rows)])

    # Extract components and add them as new columns
    table = (
        table
        .addfield('day_of_month', lambda row: row['date'].day)
        .addfield('month', lambda row: row['date'].month)
        .addfield('day_of_week', lambda row: get_day_name(row['date']))
        .addfield('year', lambda row: row['date'].year)
        .addfield('week_of_month', lambda row: (row['date'].day - 1) // 7 + 1)
        .addfield('day_of_year', lambda row: row['date'].timetuple().tm_yday)
        .addfield('week_of_year', lambda row: row['date'].isocalendar()[1])
    )
    print(table)
    return table
