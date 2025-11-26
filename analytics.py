import pandas as pd
import matplotlib.pyplot as plt

# Load the logged CSV file
df = pd.read_csv("sensor_log.csv")

# Convert timestamp column to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

plt.plot(df["timestamp"], df["temperature"])
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Trends Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
