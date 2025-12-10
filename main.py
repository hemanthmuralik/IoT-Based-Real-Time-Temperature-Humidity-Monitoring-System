import time
import csv
import random # specific for testing without hardware, replace with 'import Adafruit_DHT' for real Pi
from datetime import datetime

# --- CONFIGURATION ---
SENSOR_PIN = 4
LOG_FILE = "sensor_log.csv"
SAMPLE_INTERVAL = 2  # Seconds

# Hardware Setup (Uncomment these lines on actual Raspberry Pi)
# import Adafruit_DHT
# SENSOR = Adafruit_DHT.DHT11

def get_sensor_data():
    """
    Reads data from the DHT11 sensor.
    Returns: humidity, temperature
    """
    # --- REAL HARDWARE CODE (Uncomment below) ---
    # humidity, temperature = Adafruit_DHT.read_retry(SENSOR, SENSOR_PIN)
    # return humidity, temperature

    # --- SIMULATION CODE (For testing without Pi) ---
    # Simulates a fluctuation around 25C and 50% humidity
    temp = round(random.uniform(20.0, 30.0), 1)
    hum = round(random.uniform(40.0, 60.0), 1)
    return hum
