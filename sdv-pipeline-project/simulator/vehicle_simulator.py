
import time
import random
import requests
import json

# Ditto endpoint (example)
DITTO_URL = "http://localhost:8080/api/2/things/vehicle:car1"

while True:
    vehicle_data = {
        "speed": random.randint(40, 90),
        "steering_angle": random.randint(-20, 20),
        "battery_level": random.randint(50, 100),
        "tire_pressure": random.randint(30, 35)  # functional modification
    }

    print("Sending vehicle data:", vehicle_data)

    try:
        requests.put(
            DITTO_URL,
            headers={"Content-Type": "application/json"},
            data=json.dumps(vehicle_data)
        )
    except Exception as e:
        print("Error sending data:", e)

    time.sleep(2)
