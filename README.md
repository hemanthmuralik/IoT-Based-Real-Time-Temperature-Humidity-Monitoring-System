# IoT-Based Real-Time Temperature & Humidity Monitoring System

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red)
![Hardware](https://img.shields.io/badge/Hardware-DHT11%20%7C%20OLED-green)

An embedded IoT system that monitors environmental data in real-time using a **Raspberry Pi**, visualizing the output on an **OLED Display**. This project demonstrates the integration of sensor data acquisition, I2C communication protocols, and Python-based embedded programming.



## 📋 Overview

In industrial and agricultural sectors, maintaining specific environmental conditions is critical. This project provides a low-cost, scalable solution for monitoring **Temperature** and **Humidity**. It bridges the gap between raw sensor data and human-readable visualization using the I2C protocol.

**Key Features:**
* **Real-Time Sensing:** Data acquisition every 2 seconds using the DHT11 sensor.
* **Visual Interface:** Custom Python driver to render text and graphics on the SSD1306 OLED.
* **Efficient Communication:** Utilizes the I2C protocol for display management, freeing up GPIO pins.
* **Robustness:** Includes error handling for sensor timeouts and read failures.

## 🛠️ Tech Stack & Hardware

* **Microcomputer:** Raspberry Pi 3B+ / 4
* **Sensors:** DHT11 (Temperature & Humidity)
* **Display:** 0.96" OLED (128x64 pixels)
* **Communication:** I2C Protocol, GPIO
* **Language:** Python 3

## ⚙️ Circuit Diagram

| Component | Raspberry Pi Pin | Description |
| :--- | :--- | :--- |
| **DHT11 VCC** | 3.3V | Power |
| **DHT11 Data** | GPIO 4 | Signal |
| **OLED SDA** | GPIO 2 (SDA) | I2C Data |
| **OLED SCL** | GPIO 3 (SCL) | I2C Clock |

## 🚀 Future Scope (Edge AI Integration)

This project serves as the data acquisition layer for a larger **"Smart Environment"** system. Future plans include:
1.  **Anomaly Detection:** Integrating a lightweight **TensorFlow Lite** model to predict equipment overheating based on temperature trends.
2.  **Cloud Logging:** Pushing data to AWS IoT Core for remote monitoring.

## 🤝 Contributing

Contributions are welcome! Please fork the repo and submit a pull request.

---
**Author:** [Hemanth Murali K](https://github.com/hemanthmuralik)
