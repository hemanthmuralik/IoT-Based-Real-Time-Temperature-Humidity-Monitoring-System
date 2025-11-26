# Temperature & Humidity Monitoring System (Raspberry Pi + DHT11 + 128x64 OLED)

A complete IoT-ready temperature and humidity monitoring system using:

- Raspberry Pi
- DHT11 sensor
- 128×64 OLED (SSD1306)
- Python

---

## Features
- Real-time temperature & humidity display
- Error handling for sensor failures
- OLED display update every second
- Clean and modular Python code
- Easy to extend for IoT (MQTT, Firebase, Blynk)

---

## Circuit Connections

### DHT11 → Raspberry Pi
```
DHT11 VCC → 5V  
DHT11 GND → GND  
DHT11 DATA → GPIO4  
```

### OLED (SSD1306 I2C) → Raspberry Pi
```
OLED VCC → 3.3V  
OLED GND → GND  
OLED SDA → GPIO2  
OLED SCL → GPIO3  
```

---

## Installation

### Enable I2C
```
sudo raspi-config
Interfacing Options → I2C → Enable
sudo reboot
```

### Install Required Libraries
```
pip3 install Adafruit_DHT
pip3 install Adafruit-SSD1306
pip3 install Pillow
pip3 install smbus
```

---

## Run Program
```
python3 main.py
```

---

## Future Upgrades
- Add MQTT / ESP32 IoT dashboard
- Store data in a CSV / SQLite database
- Push alerts using Telegram bot
- Web dashboard with Flask
