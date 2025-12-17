import streamlit as st
import pandas as pd
from agents.orchestrator import run_pipeline

st.set_page_config(page_title="3D In‑Vitro BD Lead Engine", layout="wide")

st.title("3D In‑Vitro Models – BD Lead Intelligence")

with st.sidebar:
    st.header("Search Criteria")
    keywords = st.text_input("Scientific Keywords", "DILI, 3D in‑vitro, Toxicology")
    run = st.button("Run Agent")

if run:
    with st.spinner("Running web intelligence agent..."):
        df = run_pipeline(keywords)
        st.success(f"Found {len(df)} ranked leads")

        st.dataframe(df, use_container_width=True)
        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "ranked_leads.csv",
            "text/csv"
        )