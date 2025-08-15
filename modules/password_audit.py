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
    st.title("Weak Password Audit")

    pw_list = st.text_area("Enter passwords (one per line):")

    if st.button("Check"):
        results = []
        for pw in pw_list.splitlines():
            if not pw.strip():
                continue
            strength = check_strength(pw)
            results.append({"Password": pw, "Strength": strength})

        df = pd.DataFrame(results)
        st.dataframe(df)

if __name__ == "__main__":
    run()
