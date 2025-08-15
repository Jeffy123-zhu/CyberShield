# CyberShield

##  Project Screenshots

### Traffic Monitor
![Traffic Monitor](docs/exports/traffic_monitor_demo.png)

### Phishing URL Check
![Phishing Check](docs/exports/phishing_check_demo.png)

### Weak Password Audit
![Password Audit](docs/exports/password_audit_demo.png)

---

##  Sample Database Files
- [Traffic Monitor CSV](docs/exports/traffic_log_sample.csv)
- [Phishing Check CSV](docs/exports/phishing_check_sample.csv)
- [Password Audit CSV](docs/exports/password_audit_sample.csv)

---

##  About the Project
CyberShield is a **student-friendly network security visualization tool** designed and developed independently by a high school student.  
It includes three main modules:
- **Traffic Monitor** (simulation mode) – Displays simulated network traffic in real time
- **Phishing URL Check** – Detects suspicious URLs
- **Weak Password Audit** – Tests password strength and flags weak passwords

---

##  How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
