password_df.to_csv("docs/exports/password_audit_sample.csv", index=False)
import streamlit as st
import pandas as pd

def check_strength(pw):
    if len(pw) < 6:
        return "Weak"
    elif pw.isdigit() or pw.isalpha():
        return "Medium"
    else:
        return "Strong"

def run():
    st.title("弱口令审计")

    pw_list = st.text_area("输入密码（每行一个）：")
    if st.button("检测"):
        results = []
        for pw in pw_list.splitlines():
            if not pw.strip():
                continue
            strength = check_strength(pw)
            results.append({"Password": pw, "Strength": strength})
        
        df = pd.DataFrame(results)
        st.dataframe(df)
