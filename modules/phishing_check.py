import streamlit as st
import pandas as pd
import tldextract

SUSPICIOUS_KEYWORDS = ["login", "verify", "account", "secure", "update"]

def run():
    st.title("钓鱼网址检测")

    urls = st.text_area("输入网址（每行一个）：")
    if st.button("检测"):
        results = []
        for url in urls.splitlines():
            if not url.strip():
                continue
            ext = tldextract.extract(url)
            domain = f"{ext.domain}.{ext.suffix}"
            label = "Benign"
            for kw in SUSPICIOUS_KEYWORDS:
                if kw in url.lower():
                    label = "Suspicious"
                    break
            results.append({"URL": url, "Domain": domain, "Result": label})
        
        df = pd.DataFrame(results)
        st.dataframe(df)
