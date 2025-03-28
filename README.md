OBD-II Vehicle Diagnostic Tool

📌 Overview

This Python script connects to an OBD-II adapter and retrieves real-time vehicle diagnostics data. It checks key vehicle parameters such as engine RPM, speed, coolant temperature, and more. It also scans for diagnostic trouble codes (DTCs) and displays them if found.

🚀 Features

Connects to an OBD-II adapter via Python

Retrieves real-time vehicle data

Checks critical parameters like RPM, speed, and coolant temperature

Displays diagnostic trouble codes (DTCs) if any

Supports English and Arabic output for better accessibility

🛠️ Requirements

Python 3.x

obd Python package (for OBD-II communication)

An ELM327-compatible OBD-II adapter (Bluetooth, USB, or Wi-Fi)

📦 Installation

Install Python dependencies:

pip install obd

Connect your OBD-II adapter to your computer or Raspberry Pi.

▶️ Usage

Run the script using Python:

python obd_diagnostic.py

📊 Supported Parameters

The script checks the following vehicle parameters:

Engine RPM (Revolutions Per Minute)

Speed (km/h)

Coolant Temperature (°C)

Throttle Position (%)

Mass Air Flow Sensor (g/s)

Intake Pressure (kPa)

Oxygen Sensor (mA)

It also scans for Diagnostic Trouble Codes (DTCs) and displays them if any are found.

🌍 Multilingual Support

The output is displayed in English and Arabic for broader accessibility.

🔗 References

Python OBD Library

ELM327 OBD-II Adapter Information

📧 Contact

For questions or issues, feel free to reach out!

Enjoy diagnosing your vehicle with this OBD-II tool! 🚗💨

