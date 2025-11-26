import time
import csv
from datetime import datetime
import Adafruit_DHT
import RPi.GPIO as GPIO
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

# ------------------------------------
# Sensor & OLED Setup
# ------------------------------------
sensor = Adafruit_DHT.DHT11
pin = 4  # GPIO pin for DHT11

serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

# LED for alert
LED_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# CSV log file
LOG_FILE = "sensor_data.csv"

# Create CSV with header if missing
try:
    with open(LOG_FILE, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature_C", "humidity_percent"])
except FileExistsError:
    pass


def log_data(temp, hum):
    """Log temperature & humidity with timestamp."""
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), temp, hum])


# ------------------------------------
# Main Program Loop
# ------------------------------------
while True:
    hum, temp = Adafruit_DHT.read_retry(sensor, pin)

    with canvas(device) as draw:
        if hum and temp:
            draw.text((0, 0), f"Temp: {temp}°C", fill="white")
            draw.text((0, 15), f"Hum:  {hum}%", fill="white")

            # Save the reading
            log_data(temp, hum)

            # ------------------------------------
            # SMART LOGIC (Edge Intelligence)
            # ------------------------------------
            if temp > 30:
                draw.text((0, 35), "!!! HIGH TEMP !!!", fill="white")
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)

        else:
            draw.text((0, 0), "Sensor Error!", fill="white")

    time.sleep(60)  # Log once per minute
