# CyberShield

## Project Overview
CyberShield is a small project I built in high school to explore how basic cybersecurity tools work in practice.  
I wanted something simple that could show network activity and common security risks in a way that students like me could understand.

## Key Features
- **Traffic Monitor (Simulation Mode)** – Generates and shows sample network traffic, with simple charts to visualize unusual activity.  
- **Phishing URL Check** – A basic function that flags URLs containing suspicious keywords.  
- **Weak Password Audit** – Compares user input with a list of common weak passwords and gives feedback.

## How It Works
I wrote the project mainly in Python. For example:
- Used `scapy` to simulate packets.  
- Stored data with `pandas` and exported to CSV.  
- Visualized results using `matplotlib`.  

## What I Learned
Through this project, I practiced how to collect, analyze, and display data in a security context.  
It also gave me an idea of how real-world tools might detect threats, even though my version is very basic.  
If I had more time, I’d like to expand it with machine learning methods for detecting anomalies.

## Project Screenshots

### Traffic Monitor
![Traffic Monitor](docs/exports/traffic_monitor_demo.png)

### Phishing URL Check
![Phishing Check](docs/exports/phishing_check_demo.png)

### Weak Password Audit
![Password Audit](docs/exports/password_audit_demo.png)

## Sample Database Files
- [Traffic Monitor CSV](docs/exports/traffic_log_sample.csv)  
- [Phishing Check CSV](docs/exports/phishing_check_sample.csv)  
- [Password Audit CSV](docs/exports/password_audit_sample.csv)  

## How to Run
pip install -r requirements.txt
streamlit run app.py
