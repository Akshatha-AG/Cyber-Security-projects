import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Leakage Detection Dashboard", layout="centered")

st.title("🛡️ Dark Web Leak Alert System")

if os.path.exists("leak_results.csv"):
    df = pd.read_csv("leak_results.csv")
    st.dataframe(df)
    st.success("Detected leaks are shown above.")
else:
    st.info("No leak records found yet. System is secure.")
