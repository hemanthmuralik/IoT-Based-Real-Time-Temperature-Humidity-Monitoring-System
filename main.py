import Adafruit_DHT
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import time

# OLED setup
WIDTH = 128
HEIGHT = 64
RST = None

display = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
display.begin()
display.clear()
display.display()

image = Image.new('1', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)
font = ImageFont.load_default()

# DHT11 setup
SENSOR = Adafruit_DHT.DHT11
GPIO_PIN = 4   # DATA → GPIO4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(SENSOR, GPIO_PIN)

    # Clear screen
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

    if humidity is not None and temperature is not None:
        draw.text((0, 10), f"Temperature: {temperature:.1f} C", font=font, fill=255)
        draw.text((0, 30), f"Humidity: {humidity:.1f} %", font=font, fill=255)
    else:
        draw.text((10, 20), "Sensor Error!", font=font, fill=255)

    display.image(image)
    display.display()
    time.sleep(1)
