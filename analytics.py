import csv
import statistics

LOG_FILE = "sensor_log.csv"

def load_data():
    """Reads the CSV log and returns lists of temperatures and timestamps."""
    timestamps = []
    temps = []
    
    try:
        with open(LOG_FILE, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                timestamps.append(row['Timestamp'])
                temps.append(float(row['Temperature_C']))
        return timestamps, temps
    except FileNotFoundError:
        print("No data log found. Run main.py first.")
        return [], []

def calculate_moving_average(data, window_size=3):
    """
    Calculates the Simple Moving Average (SMA) to smooth sensor noise.
    """
    if len(data) < window_size:
        return data
    
    moving_averages = []
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        avg = sum(window) / window_size
        moving_averages.append(round(avg, 2))
        
    return moving_averages

def detect_anomalies(data, threshold=30.0):
    """
    Basic Anomaly Detection: Flags any temperature above a threshold.
    Returns a list of indices where anomalies occurred.
    """
    anomalies = []
    for index, value in enumerate(data):
        if value > threshold:
            anomalies.append((index, value))
    return anomalies

def generate_report():
    print("\n--- DATA ANALYTICS REPORT ---")
    timestamps, temps = load_data()
    
    if not temps:
        print("No data available to analyze.")
        return

    # Basic Stats
    avg_temp = statistics.mean(temps)
    max_temp = max(temps)
    min_temp = min(temps)
    
    print(f"Total Readings: {len(temps)}")
    print(f"Average Temp:   {avg_temp:.2f} C")
    print(f"Max Temp:       {max_temp} C")
    print(f"Min Temp:       {min_temp} C")
    
    # Advanced: Anomaly Detection
    anomalies = detect_anomalies(temps, threshold=28.0)
    if anomalies:
        print(f"\n[ALERT] {len(anomalies)} Anomalies Detected (>28.0 C):")
        for idx, val in anomalies:
            print(f"  - Reading #{idx+1}: {val} C")
    else:
        print("\n[OK] No temperature anomalies detected.")

if __name__ == "__main__":
    generate_report()
