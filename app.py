import streamlit as st, pandas as pd, random, tldextract
from datetime import datetime

bad_kw = ["login","verify","account","secure","update"]
bad_tld = ["ru","cn","xyz","top","gq","ml"]

def traffic():
    st.title("Traffic Monitor")
    random.seed(datetime.now().microsecond)
    df = pd.DataFrame({
        "Src": [f"192.168.0.{i}" for i in range(1,6)],
        "Dst": [f"10.0.0.{i}" for i in range(1,6)],
        "Proto": random.choices(["TCP","UDP","HTTP","HTTPS"], k=5),
        "Bytes": [random.randint(100,5000) for _ in range(5)]
    })
    st.dataframe(df); st.bar_chart(df["Bytes"])

def phishing():
    st.title("Phishing Check")
    urls = st.text_area("URLs:"); res=[]
    if st.button("Check URLs"):
        for u in urls.splitlines():
            if not u.strip(): continue
            ext = tldextract.extract(u)
            label, score = "Benign", 0
            if any(k in u.lower() for k in bad_kw): label, score = "Suspicious", score+50
            if ext.suffix in bad_tld: label, score = "Suspicious", score+30
            if len(u) > 70: score += 20
            if score>100: score=100
            res.append({"URL":u,"Domain":f"{ext.domain}.{ext.suffix}","Label":label,"Risk":score})
        st.dataframe(pd.DataFrame(res))

def password():
    st.title("Weak Password Audit")
    pw = st.text_area("Passwords:"); res=[]
    if st.button("Check Passwords"):
        for p in pw.splitlines():
            if not p.strip(): continue
            if len(p)<6: s="Weak"
            elif p.isdigit() or p.isalpha(): s="Medium"
            else: s="Strong"
            res.append({"Password":p,"Strength":s})
        st.dataframe(pd.DataFrame(res))

st.sidebar.title("CyberShield")
opt = st.sidebar.radio("Feature", ["Traffic","Phishing","Password"])
if opt=="Traffic": traffic()
elif opt=="Phishing": phishing()
else: password()
