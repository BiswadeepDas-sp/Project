import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def random_date(start, end):
    """Generate a random datetime between two dates."""
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

def generate_data_with_errors(num_rows=2000, output_file=r"data\data_with_errors.csv"):
    """Generate random weather data with intentional errors and missing values."""
    locations = ["San Diego", "Philadelphia", "San Antonio", "New York", "Chicago","Boston","Los Angeles","Dallas","Houston","Miami"]
    start_date = datetime(2024, 1, 1)
    end_date = datetime(2024, 12, 31)
    
    data = []
    for _ in range(num_rows):
        location = random.choice(locations)
        date_time = random_date(start_date, end_date)
        temperature = np.random.uniform(-70, 70)  # Introduce errors: unrealistic temperatures
        humidity = np.random.uniform(-20, 120)   # Introduce errors: unrealistic humidity
        precipitation = max(0, np.random.uniform(-10, 20))  # Random precipitation
        wind_speed = np.random.uniform(-10, 50)  # Introduce errors: unrealistic wind speeds

        # Randomly replace values with NaN to simulate missing data
        if random.random() < 0.1:  # 10% chance of missing temperature
            temperature = np.nan
        if random.random() < 0.1:  # 10% chance of missing humidity
            humidity = np.nan
        if random.random() < 0.05:  # 5% chance of missing precipitation
            precipitation = np.nan
        if random.random() < 0.05:  # 5% chance of missing wind speed
            wind_speed = np.nan

        data.append([location, date_time, temperature, humidity, precipitation, wind_speed])
    
    # Create DataFrame
    df = pd.DataFrame(data, columns=["Location", "Date_Time", "Temperature_C", "Humidity_pct", "Precipitation_mm", "Wind_Speed_kmh"])
    
    # Save to CSV
    df.to_csv(output_file, index=False)
    print(f"Data with errors saved to {output_file}")
    
generate_data_with_errors()

