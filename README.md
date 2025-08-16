# CyberShield

## Overview
CyberShield is a project I built independently in high school to practice basic cybersecurity concepts.  
It shows how threats like unusual traffic, phishing links, weak passwords, and network vulnerabilities can be detected and visualized.  

## Features & Demos

- **Traffic Monitor (Simulation)** – generates sample network packets and displays traffic charts.  
  ![Traffic Monitor Demo](traffic_monitor_demo.png)

- **Phishing URL Check** – flags suspicious URLs using keyword matching.  
  ![Phishing Check Demo](phishing_check_demo.png)

- **Weak Password Audit** – tests inputs against common weak passwords.  
  ![Password Audit Demo](password_audit_demo.png)

- **Port Scanning Simulation** – visualizes open ports on a target host.  
  ![Port Scan Demo](port_scan.png)

- **Anomaly Detection Chart** – summarizes unusual activity.  
  ![Anomaly Chart](anomaly_chart.png)

- **Dashboard Overview** – central interface showing all metrics.  
  ![Dashboard](dashboard.png)

> All demos can be run locally with Python; no external servers are required.

## How It Works
Written in Python using:  
- `scapy` – simulates and analyzes network packets  
- `pandas` – handles and exports data  
- `matplotlib` – creates visualizations  

Sample data is dynamically generated and exportable as CSV, making the project reproducible.

## Reflection
This was my first full project combining programming and cybersecurity.  
It demonstrates how small scripts can model real-world security issues.  
I plan to expand it in the future with more advanced detection, possibly using machine learning.
