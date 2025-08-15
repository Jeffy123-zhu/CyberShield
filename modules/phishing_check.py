import streamlit as st
import pandas as pd
import tldextract

SUSPICIOUS_KEYWORDS = ["login", "verify", "account", "secure", "update"]

def run():
    st.title("phishing site monitoring")

    urls = st.text_area("Enter the URL（one per line）：")
    if st.button("check"):
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
