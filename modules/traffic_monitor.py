df.to_csv("docs/exports/traffic_log_sample.csv", index=False)

import streamlit as st
import pandas as pd
import random

def run():
    st.title("网络流量监控（模拟模式）")

    data = {
        "源IP": [f"192.168.0.{i}" for i in range(1, 6)],
        "目标IP": [f"10.0.0.{i}" for i in range(1, 6)],
        "协议": random.choices(["TCP", "UDP", "HTTP", "HTTPS"], k=5),
        "字节数": [random.randint(100, 5000) for _ in range(5)]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df["字节数"])
