import os

os.makedirs("docs/exports", exist_ok=True)

import streamlit as st
from modules import traffic_monitor, phishing_check, password_audit

st.set_page_config(page_title="CyberShield Student Edition", layout="wide")

st.sidebar.title("CyberShield Menu")
choice = st.sidebar.radio(
    "选择功能模块：",
    ["Traffic Monitor", "Phishing Check", "Weak Password Audit"]
)

if choice == "Traffic Monitor":
    traffic_monitor.run()
elif choice == "Phishing Check":
    phishing_check.run()
elif choice == "Weak Password Audit":
    password_audit.run()
