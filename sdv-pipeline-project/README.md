
# Software Defined Vehicle (SDV) Pipeline

This project demonstrates a simple Software Defined Vehicle pipeline using:

- Eclipse Kuksa
- Eclipse Zenoh
- Eclipse Ditto

Pipeline Architecture:

Vehicle Simulator
↓
Eclipse Kuksa
↓
Zenoh Middleware
↓
Eclipse Ditto (Digital Twin Backend)
↓
Monitoring via API

Vehicle Signals:

- speed
- steering_angle
- battery_level
- tire_pressure (functional modification)

Requirements:

- Docker Desktop
- Python 3
- Python package: requests

Install dependency:

pip install requests

Running the System:

Start Kuksa:

bash scripts/start_kuksa.sh

Start Zenoh:

bash scripts/start_zenoh.sh

Start Ditto:

bash scripts/start_ditto.sh

Run the vehicle simulator:

python simulator/vehicle_simulator.py

Verify Data Flow:

curl http://localhost:8080/api/2/things/vehicle:car1
