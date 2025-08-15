import streamlit as st
import pandas as pd
import random
from datetime import datetime
def run():
    st.title("Network Traffic Monitoring (Simulate Mode)")
    st.caption("Demo data generated locally for testing purposes.")

    random.seed(datetime.now().microsecond)

    traffic_data = {
        "Source IP": [f"192.168.0.{i}" for i in range(1, 6)],  
        "Target IP": [f"10.0.0.{i}" for i in range(1, 6)],   
        "Protocol": random.choices(["TCP", "UDP", "HTTP", "HTTPS"], k=5),  
        "Bytes": [random.randint(100, 5000) for _ in range(5)]  
    }

    df = pd.DataFrame(traffic_data)

    st.subheader("Traffic Table")
    st.dataframe(df)

    st.subheader("Traffic Size Bar Chart")
    st.bar_chart(df["Bytes"])

if __name__ == "__main__":
    run()
