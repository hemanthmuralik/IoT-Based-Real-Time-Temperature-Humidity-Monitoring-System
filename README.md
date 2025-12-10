# 📡 Edge Environmental Logger & Analytics Node

![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-red) ![Language](https://img.shields.io/badge/Python-3.x-blue) ![Focus](https://img.shields.io/badge/Focus-Data%20Engineering%20%7C%20Edge%20AI-green) ![License](https://img.shields.io/badge/License-MIT-orange)

> A robust, edge-computing node that captures, logs, and analyzes environmental time-series data locally. Designed as a foundational data acquisition layer for Smart Building applications.

---

## 📖 Overview

The **Edge Environmental Logger** is more than just a monitoring system; it is a complete **Data Acquisition Pipeline**. 

Running on a Raspberry Pi, it interfaces with industrial-grade sensors to capture high-resolution environmental data (Temperature & Humidity). Unlike standard IoT demos, this system implements **persistent data storage (CSV Logging)** and **on-device statistical analysis**, bridging the gap between hardware sensing and AI-ready datasets.

### 🚀 Key Capabilities
* **Time-Series Data Logging:** Automatically stamps and saves sensor readings to a structured CSV dataset (`sensor_log.csv`) for historical analysis.
* **Edge Analytics Engine:** Features a dedicated analytics module (`analytics.py`) that computes **Moving Averages** to smooth sensor noise.
* **Anomaly Detection:** Implements algorithmic logic to flag outlier events (e.g., sudden temperature spikes indicating equipment failure).
* **Resilient Design:** Includes error handling for sensor timeouts and I2C communication failures.

---

## ⚙️ Technical Architecture

The system follows a modular "Sense-Log-Analyze" architecture:

```mermaid
graph LR
    A[DHT11 Sensor] -->|GPIO Signal| B(Raspberry Pi Node)
    B -->|Real-Time| C[OLED Display]
    B -->|Time-Series Data| D[(CSV Database)]
📂 Project Structure
.
├── main.py          # Core logic: Sensor reading, OLED rendering, & Data Logging
├── analytics.py     # AI Module: Moving Average smoothing & Anomaly Detection
├── requirements.txt # Python dependencies
├── sensor_log.csv   # The generated dataset (Time-Series)
└── README.md        # Documentation
 Data & Analytics DemoThe system generates a structured dataset ready for Machine Learning.1. Raw Data Sample (sensor_log.csv):Code snippetTimestamp,Temperature_C,Humidity_Pct
2025-12-10 09:00:01, 24.5, 45.2
2025-12-10 09:00:03, 24.6, 45.1
2025-12-10 09:00:05, 80.0, 45.0  <-- ANOMALY DETECTED
2. Analytics Output:Running python3 analytics.py processes the log and generates insights:Plaintext--- DATA ANALYTICS REPORT ---
Total Readings: 1500
Average Temp:   24.8 C
[ALERT] 1 Anomaly Detected (>30.0 C):
  - Reading #450: 80.0 C (Possible Fire/Sensor Error)
🛠️ Hardware SetupComponentPin ConnectionProtocolDHT11 SensorGPIO 4One-WireOLED DisplayGPIO 2 (SDA) / GPIO 3 (SCL)I2C🚀 Getting StartedClone the Repository:Bashgit clone [https://github.com/hemanthmuralik/Edge-Environmental-Logger.git](https://github.com/hemanthmuralik/Edge-Environmental-Logger.git)
cd Edge-Environmental-Logger
Install Dependencies:Bashpip3 install -r requirements.txt
Run the Data Logger:Bashpython3 main.py
The system will start printing live data and saving it to sensor_log.csv.Run Analytics:Bashpython3 analytics.py
👨‍💻 AuthorHemanth Murali K Electronics Engineer & Aspiring AI Product ManagerLinkedIn | GitHub
    D -->|Batch Processing| E[Analytics Engine]
    E -->|Output| F[Statistical Report & Anomalies]
