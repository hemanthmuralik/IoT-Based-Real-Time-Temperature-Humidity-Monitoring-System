import time
import csv
from datetime import datetime
import Adafruit_DHT
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

# Sensor setup
sensor = Adafruit_DHT.DHT11
pin = 4   # GPIO pin where DHT11 is connected

# OLED setup
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

LOG_FILE = "sensor_log.csv"

# Create CSV header if file doesn't exist
try:
    with open(LOG_FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity"])
except FileExistsError:
    pass


def log_data(temp, hum):
    """Append data to CSV file."""
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), temp, hum])


while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)

    with canvas(device) as draw:
        if hum and temp:
            # Display values
            draw.text((0, 0), f"T: {temp}°C", fill="white")
            draw.text((0, 15), f"H: {hum}%", fill="white")

            # Log sensor data
            log_data(temp, hum)

            # High temperature warning
            if temp > 30:
                draw.text((0, 35), "WARNING: HIGH TEMP!", fill="white")

        else:
            draw.text((0, 0), "Sensor Error", fill="white")

    # Read & log every 10 minutes
    time.sleep(600)
