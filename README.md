# CyberShield

## Project Overview
I developed **CyberShield**, a student-friendly network security visualization tool, independently during high school.  
This project demonstrates my hands-on skills in network monitoring, phishing detection, and password auditing using real and simulated data.

## Key Features
- **Traffic Monitor (Simulation Mode)** – Displays simulated network traffic in real time, helping visualize potential threats.  
- **Phishing URL Check** – Detects suspicious URLs and flags potential phishing attempts.  
- **Weak Password Audit** – Tests password strength and highlights weak passwords for better security awareness.

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
