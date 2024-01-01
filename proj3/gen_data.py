import csv
from datetime import datetime

def generate_dates(year):
    dates = []
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date = f"{day:02d}/{month:02d}/{year}"
                datetime.strptime(date, "%d/%m/%Y")
                dates.append((day, month))
            except ValueError:
                pass
    return dates

def save_dates_to_csv(dates, filepath):
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Day", "Month"])
        writer.writerows(dates)

year = 2023
dates = generate_dates(year)
save_dates_to_csv(dates, "./dates.csv")
